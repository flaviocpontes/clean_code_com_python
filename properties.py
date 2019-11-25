import re

EMAIL_FORMAT = re.compile(r'[^@]+@[^@]+\.[^@]+')


def validate_email(email: str):
    if re.match(EMAIL_FORMAT, email):
        return email

    raise ValueError(f'{email} is not a valid email address')


class User:
    def __init__(self, email):
        self._email = validate_email(email)

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        self._email = validate_email(new_email)

