import os
from dotenv import load_dotenv

load_dotenv()


class Data:
    admin_email = os.getenv('ADMIN_LOGIN')
    admin_password = os.getenv('ADMIN_PASSWORD')
    admin_email_invalid = os.getenv('ADMIN_LOGIN_INVALID')
    admin_password_invalid = os.getenv('ADMIN_PASSWORD_INVALID')
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')
    phone_number = os.getenv('PHONE_NUMBER')
    name = os.getenv('NAME')
    email_invalid = os.getenv('INVALID_EMAIL')
    password_invalid = os.getenv('INVALID_PASSWORD')
