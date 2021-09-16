#!/usr/bin/python3
'''
Module contains a fab script to generates a .tgz archive from the contents
of the web_static
'''
from fabric.api import local, env, put, run, lcd, cd
import os
import time

env.user = 'ubuntu'
env.hosts = ['34.75.214.109', '35.190.185.74']


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


def do_deploy(archive_path):
    '''
    Distributes an archive to my webservers
    '''
    if not os.path.isfile(archive_path):
        return False

    # Upload the archive to the server
    put(archive_path, '/tmp/')

    # Create directory where we will extract the file to
    file_name = archive_path.split('/')[-1]  # Get file name
    dir_path = '/data/web_static/releases/{}'.format(file_name.split('.')[0])
    run('mkdir -p {}'.format(dir_path))

    # Uncompress the archive to the folder
    server_archive_path = '/tmp/' + file_name  # Path of archive in server
    run('tar -xzf {} -C {}'.format(server_archive_path, dir_path))

    # Delete the archive from the web server
    run('rm -rf {}'.format(server_archive_path))

    # Delete the symbolic link
    run('rm -rf /data/web_static/current')

    # Move the files from web_static to web_static_<number>
    run('mv {}/web_static/* {}'.format(dir_path, dir_path))
    run('rm -rf {}/web_static'.format(dir_path))

    # Create a new symbolic link
    run('ln -s {} /data/web_static/current'.format(dir_path))

    return True


def deploy():
    '''
    Deploys my webstatic files to my servers
    '''
    archive_path = do_pack()
    if not archive_path:
        return False

    return do_deploy(archive_path)


def do_clean(number=0):
    '''
    Deletes out of date archives
    args:
        number(int): The number of archives to keep
    '''
    # Convert the number to an int
    number = int(number)

    # Make a sorted list of the files
    files = os.listdir("versions")
    files.sort()

    # Filter the list to remain with only files we are going to delete
    if number == 0 or number == 1:
        files.pop()
    else:
        for i in range(number):
            files.pop()

    # Delete the files locally and also on the server
    with lcd('versions'):
        for f in files:
            local('rm {}'.format(f))

    with cd('/data/web_static/releases'):
        for f in files:
            run('rm -rf {}'.format(f.split('.'[0])))
