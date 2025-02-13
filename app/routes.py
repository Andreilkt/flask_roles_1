# import required libraries from flask_login and flask_security
from flask_login import LoginManager, login_manager, login_user, logout_user
from flask_security import Security, SQLAlchemySessionUserDatastore, roles_accepted
from app import app
from app.models import Role, User, db, roles_users




# load users, roles for a session
user_datastore = SQLAlchemySessionUserDatastore(db.session, User, Role)
security = Security(app, user_datastore)

# import the required libraries
from flask import render_template, redirect, url_for

# ‘/’ URL is bound with index() function.
@app.route('/')
# defining function index which returns the rendered html code
# for our home page
def index():
    return render_template("index.html")


# import 'request' to request data from html
from flask import request

# import 'request' to request data from html
from flask import request


# signup page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    msg = ""
    # if the form is submitted
    if request.method == 'POST':
        # check if user already exists
        user = User.query.filter_by(email=request.form['email']).first()
        msg = ""
        # if user already exists render the msg
        if user:
            msg = "User already exist"
            # render signup.html if user exists
            return render_template('signup.html', msg=msg)

        # if user doesn't exist

        # store the user to database
        user = User(email=request.form['email'], active=1, password=request.form['password'])
        # store the role
        role = Role.query.filter_by(id=request.form['options']).first()
        user.roles.append(role)

        # commit the changes to database
        db.session.add(user)
        db.session.commit()

        # login the user to the app
        # this user is current user
        login_user(user)
        # redirect to index page
        return redirect(url_for('index'))

    # case other than submitting form, like loading the page itself
    else:
        return render_template("signup.html", msg=msg)


# signin page
@app.route('/signin', methods=['GET', 'POST'])
def signin():
    msg = ""
    if request.method == 'POST':
        # search user in database
        user = User.query.filter_by(email=request.form['email']).first()
        # if exist check password
        if user:
            if user.password == request.form['password']:
                # if password matches, login the user
                login_user(user)
                return redirect(url_for('index'))
            # if password doesn't match
            else:
                msg = "Wrong password"

        # if user does not exist
        else:
            msg = "User doesn't exist"
        return render_template('signin.html', msg=msg)

    else:
        return render_template("signin.html", msg=msg)


# for teachers page
@app.route('/teachers')
# only Admin can access the page
@roles_accepted('Admin')
def teachers():
    teachers = []
    # query for role Teacher that is role_id=2
    role_teachers = db.session.query(roles_users).filter_by(role_id=2)
    # query for the users' details using user_id
    for teacher in role_teachers:
        user = User.query.filter_by(id=teacher.user_id).first()
        teachers.append(user)
    # return the teachers list
    return render_template("teachers.html", teachers=teachers)


# for staff page
@app.route('/staff')
# only Admin and Teacher can access the page
@roles_accepted('Admin', 'Teacher')
def staff():
    staff = []
    role_staff = db.session.query(roles_users).filter_by(role_id=3)
    for staf in role_staff:
        user = User.query.filter_by(id=staf.user_id).first()
        staff.append(user)
    return render_template("staff.html", staff=staff)


# for student page
@app.route('/students')
# only Admin, Teacher and Staff can access the page
@roles_accepted('Admin', 'Teacher', 'Staff')
def students():
    students = []
    role_students = db.session.query(roles_users).filter_by(role_id=4)
    for student in role_students:
        user = User.query.filter_by(id=student.user_id).first()
        students.append(user)
    return render_template("students.html", students=students)


# for details page
@app.route('/mydetails')
# Admin, Teacher, Staff and Student can access the page
@roles_accepted('Admin', 'Teacher', 'Staff', 'Student')
def mydetails():
    return render_template("mydetails.html")


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('signin'))

@app.route('/delete/<int:id>', methods=['GET'])

def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('index'))
