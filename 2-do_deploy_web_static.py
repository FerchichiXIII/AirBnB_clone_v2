#!/usr/bin/python3
"""
 Fabric script that distributes an archive to your web servers
"""
from genericpath import exists
from fabric.api import *
import os


env.usr = ['35.173.249.36', '54.173.105.242']


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers
    """
    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/{}".format(no_ext)
        run("mkdir -p {}".format(path))
        put(archive_path, path)
        with cd(path):
            run("tar -xzf {}".format(file_n))
            run("rm {}".format(file_n))
            run("mv {} {}".format(no_ext, "current"))
            run("rm -rf releases/*")
            run("ln -s {} releases/current")
            run("service nginx restart")
            return True
    except Exception as e:
        print(e)
        return False
