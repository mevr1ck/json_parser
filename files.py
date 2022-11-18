import os

DIR = os.path.dirname(__file__)


def get_path(filename: str):
    return os.path.join(DIR, filename)


BOOKS_FILE = get_path(filename='books.csv')
USERS_FILE = get_path(filename='users.json')
