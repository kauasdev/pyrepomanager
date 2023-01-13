import platform
from subprocess import check_output, CalledProcessError
from .excepitions import SupportLibError, GhModuleNotFound


def check_os() -> str:
    os = platform.system()
    return os.capitalize()


def check_lib_supported() -> tuple[bool, str]:
    os_supported = ['Windows', 'Linux']
    os = check_os()
    if os in os_supported:
        return True, os
    else:
        raise SupportLibError(
            f"Pyrepomanager is not compatible with {os} OS... "
            "Please report this bug/problem at (https://github.com/kauasdev/pyrepomanager/issues)"
        )


def check_gh_installed():
    try:
        check_output(['gh'], shell=True).decode().split()
        return True
    except CalledProcessError:
        raise GhModuleNotFound("gh module not found!")
