import os

#клдасс конфигурации проекта
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'paraplan'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'  # Подключение к базе данных SQLite
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Отключение предупреждений о модификациях
    UPLOAD_FOLDER = "app/static/images"
    MAIL_SERVER = 'smtp.yandex.ru'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'andreilkt@yandex.ru'
    MAIL_DEFAULT_SENDER = 'andreilkt@yandex.ru'
    MAIL_PASSWORD = 'mqkbfoggoxxxktjn'
    # hashes the password and then stores in the database

    # allows new registrations to application
    SECURITY_REGISTERABLE = True
    # to send automatic registration email to user
    SECURITY_SEND_REGISTER_EMAIL = False



