import platform
import getpass
import socket
import os


def get_system_info():
    system_info = {
        "system": platform.system(),
        "release": platform.release(),
        "version": platform.version(),
        "username": getpass.getuser(),
        "hostname": socket.gethostname(),
        "ip_address": socket.gethostbyname(socket.gethostname()),
        "processor": platform.processor(),
        "architecture": platform.architecture(),
        "home_directory": os.path.expanduser("~"),
    }
    return system_info


print(get_system_info())
