#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the web_static
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    """
    if not os.path.exists("versions"):
        os.mkdir("versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file = "versions/web_static_{}.tgz".format(date)
    local("tar -cvzf {} web_static".format(file))
    return file
