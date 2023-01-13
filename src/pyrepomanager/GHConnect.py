import os
import os.path as path
from subprocess import check_call, CalledProcessError
import sys


class GHConnect:
    __token_file = "gh_user_token_file.txt"

    def __init__(self, gh_username: str, gh_user_token: str):
        self.__gh_username = gh_username
        self.__gh_user_token = gh_user_token
        self.__is_authenticated = False

    # Getters
    @property
    def gh_username(self):
        return self.__gh_username

    @property
    def gh_user_token(self):
        return self.__gh_user_token

    @property
    def is_authenticated(self):
        return self.__is_authenticated

    # Setters
    def __set_is_authenticated(self, value: bool):
        self.__is_authenticated = value

    @staticmethod
    def __create_token_file(file_path, token_value):
        with open(file_path, "w") as file:
            file.write(token_value)
            file.seek(0)

    @staticmethod
    def __read_token_file(file_path):
        with open(file_path, "r") as file:
            token = file.readlines()[0]
            file.seek(0)

            return token

    @staticmethod
    def __write_token_file(file_path, token_value):
        with open(file_path, "w") as file:
            file.write(token_value)
            file.seek(0)

    def __verify_or_create_token_file(self) -> str:
        if path.isfile(GHConnect.__token_file):
            token = self.__read_token_file(GHConnect.__token_file)
            if token != self.__gh_user_token:
                self.__write_token_file(GHConnect.__token_file, self.__gh_user_token)
            else:
                pass
        else:
            self.__create_token_file(GHConnect.__token_file, self.__gh_user_token)

        return GHConnect.__token_file

    def auth_gh_user(self):
        file_token_name = self.__verify_or_create_token_file()
        try:
            check_call(f"gh auth login --with-token < {file_token_name}", stderr=sys.stderr, shell=True)
            os.remove(file_token_name)
            self.__set_is_authenticated(True)
        except CalledProcessError as e:
            print(e)
            self.__set_is_authenticated(False)

    def logout_gh_user(self):
        try:
            check_call(['gh', 'auth', 'logout', '-h', 'github.com'])
            self.__set_is_authenticated(False)
        except CalledProcessError as e:
            print(e)
