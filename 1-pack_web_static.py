#!/usr/bin/python3
'''
Module contains a fab script to generates a .tgz archive from the contents
of the web_static
'''
from fabric.api import local
import os
import time


def do_pack():
    '''
    A function that generaees a .tgx archive from the web_static folder
    '''
    if not os.path.exists('versions'):
        os.makedirs('versions')

    filename = time.strftime("%Y%m%d%H%M%S")
    fullpath = "versions/web_static_{}.tgz".format(filename)
    try:
        local("tar -cvzf {} web_static".format(fullpath))
        return fullpath
    except:
        return None
