import pytest
import os
import random
import string
import json

from tech_console.login import Login


class TestAuth(object):
    @classmethod
    def setup_class(cls) -> None:
        password_file = './{}.json'.format(''.join([random.choice(string.ascii_lowercase) for _ in range(5)]))
        if os.path.exists(password_file):
            os.remove(password_file)
        cls.password_file = password_file
        cls.login_sys = Login(password_file=password_file)

    @classmethod
    def teardown_class(cls) -> None:
        os.remove(cls.password_file)

    def test_login_init(self) -> None:
        print('Testing login initialisation')
        assert os.path.exists(self.password_file)
        print('Checking that the password file is empty')
        with open(self.password_file, 'r') as jf:
            passwd_json = json.load(jf)
        assert not passwd_json

    def test_add_user(self) -> None:
        pass

    def test_successful_login(self) -> None:
        pass

    def test_failed_login(self) -> None:
        pass
