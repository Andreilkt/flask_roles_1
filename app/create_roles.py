# create_roles.py
from flask import Flask
from models import Role, db

"""Скрипт пока не  работает, но данные из него возможно использовать при создании ролей  через flask shell"""


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        # Создаем Пользователей

        admin = Role(id=1, name='Admin')
        teacher = Role(id=2, name='Teacher')
        staff = Role(id=3, name='Staff')
        student = Role(id=4, name='Student')

        db.session.add(admin)
        db.session.add(teacher)
        db.session.add(staff)

        db.session.add(student)
        db.session.add(staff)
        db.session.commit()
# def create_roles():
#     admin = Role(id=1, name='Admin')
#     teacher = Role(id=2, name='Teacher')
#     staff = Role(id=3, name='Staff')
#     student = Role(id=4, name='Student')
#
#     db.session.add(admin)
#     db.session.add(teacher)
#     db.session.add(staff)
#     db.session.add(student)
#
#     db.session.commit()
#     print("Roles created successfully!")
#
# # Function calling will create 4 roles as planned!
# create_roles()
