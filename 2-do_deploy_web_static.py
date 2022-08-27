#!/usr/bin/python3
"""
 Fabric script that distributes an archive to your web servers
"""
from fabric.api import *
import os


env.usr = ['35.173.249.36', '3.95.204.110']


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers
    """
    if not os.path.exists(archive_path):
        return False
    try:
        file_n = archive_path.split("/")[-1]
        path = archive_path.split(file_n)[0]
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}".format(path))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(file_n, path))
        run("rm /tmp/{}".format(file_n))
        run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(path, path))
        run("rm -rf /data/web_static/releases/{}/web_static".format(path))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{} /data/web_static/current".format(path))
        return True
    except:
        return False
