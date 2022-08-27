#!/usr/bin/python3
"""
 Fabric script that distributes an archive to your web servers
"""
from fabric.api import *
from datetime import datetime
import os


def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        return False
    else:
        put(archive_path, "/tmp/")
        file = archive_path.split("/")[-1]
        archive = file.split(".")[0]
        run("mkdir -p /data/web_static/releases/{}/".format(archive))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(file, archive))
        run("rm /tmp/{}".format(file))
        run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(archive, archive))
        run("rm -rf /data/web_static/releases/{}/web_static".format(archive))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(archive))
        return True
