from os import path

# Mastermind config
DEFAULT_NODE_WEIGHT = 10
INPUT_LENGTH = 5
ALLOWED_GUESSES = 5


# Console
PROMPT = 'daedalus-tech:> '

# Login
PASSWORD_FILE = path.expanduser('~/.tech_console/passwd.json')
DEFAULT_ADMIN_USERNAME = 'admin'
USER_LEVELS = {
    'admin': 0,
    'user': 10,
}
LOGIN_ATTEMPTS = 3
