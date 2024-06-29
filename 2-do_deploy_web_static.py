#!/usr/bin/python3
"""
Fabric script for deploying a web static archive to web servers
"""

from fabric import task
from os import path
from fabric.connection import Connection

env = {
    'hosts': ['142.44.167.228', '144.217.246.195'],
    'user': 'ubuntu'  # Replace with your SSH username
}

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

if __name__ == '__main__':
    # Usage example: python script.py do_deploy:/path/to/archive.tar.gz
    import sys
    if len(sys.argv) < 2:
        print("Usage: python script.py do_deploy:/path/to/archive.tar.gz")
        sys.exit(1)
    task_name, archive_path = sys.argv[1].split(':')
    c = Connection(env['hosts'][0], user=env['user'])
    result = globals()[task_name](c, archive_path)
    print("Deployment successful!" if result else "Deployment failed!")
