import os
import json
from typing import Dict, Text, Tuple, Optional, Union

import bcrypt

from .config import PASSWORD_FILE, USER_LEVELS


class Login(object):
    def __init__(self, password_file: str = PASSWORD_FILE):
        self.salt = bcrypt.gensalt()
        self.password_file = password_file
        if not os.path.exists(self.password_file):
            os.makedirs(os.path.dirname(self.password_file), exist_ok=True)
            with open(self.password_file, 'w+') as jf:
                json.dump({}, jf, indent=4, sort_keys=True)
        with open(self.password_file) as jf:
            self.passwd: Dict[Text, Dict[Text, Union[Text, int]]] = json.load(jf)

    def __write_passwd(self) -> None:
        with open(self.password_file, 'w+') as jf:
            json.dump(self.passwd, jf, indent=4, sort_keys=True)

    def add(self, user: str, passwd: str, level: int = USER_LEVELS['user']) -> None:
        self.passwd[user] = {'password': bcrypt.hashpw(passwd.encode('utf-8'), self.salt).decode('utf-8'),
                             'level': level}
        with open(self.password_file, 'w+') as jf:
            json.dump(self.passwd, jf, indent=4, sort_keys=True)

    def delete(self, user: str) -> None:
        if user not in self.passwd:
            return None
        self.passwd.pop(user)
        self.__write_passwd()

    def attempt_login(self, user: str, passwd: str) -> Tuple[bool, Optional[int]]:
        if user in self.passwd and self.passwd[user]['password'].encode('utf-8') == \
                bcrypt.hashpw(passwd.encode('utf-8'), self.passwd[user]['password'].encode('utf-8')):
            return True, self.passwd[user]['level']
        return False, None
