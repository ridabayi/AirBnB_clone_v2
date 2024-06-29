#!/usr/bin/python3
"""
Fabric script for deploying a web static archive to web servers
"""

from fabric import task
from datetime import datetime
from os import path

env = {
    'hosts': ['142.44.167.228', '144.217.246.195'],
    'user': 'ubuntu'  # Replace with your SSH username
}

@task
def do_pack():
    """Generates a compressed archive of web_static"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if not path.isdir("versions"):
            local("mkdir -p versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Error packing:", e)
        return None

@task
def do_deploy(c, archive_path):
    """Distributes an archive to the web servers"""
    if not path.exists(archive_path):
        return False
    try:
        file_name = path.basename(archive_path)
        no_ext = path.splitext(file_name)[0]
        remote_path = "/data/web_static/releases/"
        c.put(archive_path, '/tmp/')
        c.run('mkdir -p {}{}/'.format(remote_path, no_ext))
        c.run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, remote_path, no_ext))
        c.run('rm /tmp/{}'.format(file_name))
        c.run('mv {0}{1}/web_static/* {0}{1}/'.format(remote_path, no_ext))
        c.run('rm -rf {}{}/web_static'.format(remote_path, no_ext))
        c.run('rm -rf /data/web_static/current')
        c.run('ln -s {}{}/ /data/web_static/current'.format(remote_path, no_ext))
        return True
    except Exception as e:
        print("Deployment failed:", e)
        return False

@task
def deploy(c):
    """Creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(c, archive_path)
