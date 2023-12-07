#!/usr/bin/python3
# Fabfile to create and distribute an archive to a web server.
import os.path
from os import path
from datetime import datetime
from fabric.api import env, local, run, put, task



env.hosts = ["35.174.185.198", "52.201.167.109"]

@task
def deploy():
    """Create and distribute an archive to a web server."""
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)

def do_pack():
    """Generates a .tgz archive from the contents
    of the web_static folder of this repository.
    """

    d = datetime.now()
    now = d.strftime('%Y%m%d%H%M%S')

    local("mkdir -p versions")
    local("tar -czvf versions/web_static_{}.tgz web_static".format(now))

def do_deploy(archive_path):
    """Distributes an .tgz archive through web servers
    """

    if path.exists(archive_path):
        archive = archive_path.split('/')[1]
        a_path = "/tmp/{}".format(archive)
        folder = archive.split('.')[0]
        f_path = "/data/web_static/releases/{}/".format(folder)

        put(archive_path, a_path)
        run("mkdir -p {}".format(f_path))
        run("tar -xzf {} -C {}".format(a_path, f_path))
        run("rm {}".format(a_path))
        run("mv -f {}web_static/* {}".format(f_path, f_path))
        run("rm -rf {}web_static".format(f_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(f_path))

        return True

    return False