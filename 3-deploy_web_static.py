#!/usr/bin/python3
"""Fabric script to create a new instance of a class"""
from datetime import datetime
from os.path import exists, isdir
from fabric.api import *
env.hosts = ['35.173.249.36, 54.173.105.242']


def deploy():

	"""
	Deploy the latest version of the project.
	"""
	try:
		date = datetime.now().strftime("%Y%m%d%H%M%S")
		if isdir("versions") is False:
			local("mkdir versions")
		file_name = "versions/web_static_{}.tgz".format(date)
		local("tar -zcvf {} web_static".format(file_name))
		return file_name
	except:
		return False

