import os
from dotenv import load_dotenv

load_dotenv()


class Data:
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')
    phone_number = os.getenv('PHONE_NUMBER')
    name = os.getenv('NAME')
    email_invalid = os.getenv('INVALID_EMAIL')
    password_invalid = os.getenv('INVALID_PASSWORD')
