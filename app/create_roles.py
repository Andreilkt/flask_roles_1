# create_roles.py
from models import Role, db
from app import app

"""Скрипт пока не  работает, но данные из него возможно использовать при создании ролей  через flask shell"""

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
