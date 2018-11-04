#!/usr/bin/env python3
import sys
from subprocess import Popen

from prompt_toolkit import PromptSession
from prompt_toolkit import print_formatted_text as printft
from bitarray import bitarray

from .mastermind import Mastermind
from .login import Login
from .config import PROMPT, DEFAULT_ADMIN_USERNAME, USER_LEVELS, LOGIN_ATTEMPTS


class TechConsole(object):
    def __init__(self, prompt_text: str = PROMPT, debug: bool = False, login_attempts: int = LOGIN_ATTEMPTS) -> None:
        self.session = PromptSession()
        self.prompt_text = prompt_text
        self.debug = debug
        self.auth_level: int = None
        self.__max_login_atempts = login_attempts

    def runrepair(self):
        mm = Mastermind()
        printft('=== Daedalus repair console ===')
        while True:
            try:
                input_string = self.session.prompt('provide repair string: ')
            except KeyboardInterrupt:
                printft('Exiting repair console')
                break
            if input_string == 'exit':
                printft('Exiting repair console')
                break
            if not set(input_string).issubset({'0', '1'}):
                printft('Repair string should only contain "0"\'s and "1"\'s')
                continue
            input_string = bitarray(input_string)
            res = mm.guess(input_string)
            if res is None:
                printft('repaired')
            else:
                printft(res)

    @staticmethod
    def clear() -> None:
        p = Popen(['clear'])
        p.communicate()

    def add_user(self) -> None:
        if self.auth_level > USER_LEVELS['admin']:
            printft('Unauthorized for your user level')
            return 
        login_sys = Login()

    def auth(self) -> None:
        login_sys = Login()
        if not login_sys.passwd:
            printft('First run - initialise users')
            admin_user = self.session.prompt('Admin username (default: {}): '.format(DEFAULT_ADMIN_USERNAME))
            if not admin_user:
                admin_user = DEFAULT_ADMIN_USERNAME
            admin_pass = self.session.prompt('Admin password: ', is_password=True)
            while not admin_pass:
                admin_pass = self.session.prompt('Admin password: ', is_password=True)
            login_sys.add(admin_user, admin_pass, level=USER_LEVELS['admin'])
        else:
            login_attempt = 0
            while True:
                user = None
                while not user:
                    user = self.session.prompt('Username: ', is_password=False)
                password = self.session.prompt('Password: ', is_password=True)
                success, level = login_sys.attempt_login(user, password)
                if success:
                    self.auth_level = level
                    break
                login_attempt += 1
                if login_attempt == self.__max_login_atempts:
                    printft('Login attempt limit reached. Exiting')
                    self.exit(1)
                printft('Username or password incorrect. Please try again')
        self.run()

    def run(self) -> None:
        while True:
            cmd = None
            try:
                cmd = self.session.prompt(self.prompt_text, is_password=False)
            except KeyboardInterrupt:
                printft('CTRL-C pressed')
            except EOFError:
                printft('CTRL-D pressed')
            if cmd == 'exit':
                self.exit()
            if cmd == 'repair':
                self.runrepair()
            if cmd == 'clear':
                self.clear()
            printft('cmd is {}'.format(cmd))

    @staticmethod
    def exit(exit_code: int = 0) -> None:
        sys.exit(exit_code)


if __name__ == '__main__':
    console = TechConsole()
    console.auth()
