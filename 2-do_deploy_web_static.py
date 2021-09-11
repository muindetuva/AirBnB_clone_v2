#!/usr/bin/python3
'''
Module contains a fab script to distributes an archive to your web servers
'''
from fabric.api import env, run, put
import os


env.hosts = [
    '34.75.214.109',
    '35.190.185.74',
]

env.user = "ubuntu"


def do_deploy(archive_path):
    '''
    A function that distributes an archive to your web servers
    '''
    if not os.path.exists(archive_path):
        return False
    try:
        up_archive = archive_path.split("/")[-1]
        ext_archive = "/data/web_static/releases/" + up_archive.split(".")[0]
        put("{}".format(archive_path), "/tmp")
        run("mkdir {}".format(ext_archive))
        run("tar -xzf /tmp/{} -C {}".format(up_archive, ext_archive))
        run("rm -rf /tmp/{}".format(up_archive))
        run("mv {}/web_static/* {}/".format(ext_archive, ext_archive))
        run("rm -rf {}/web_static".format(ext_archive))

        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(ext_archive))

        return True
    except:
        return False
