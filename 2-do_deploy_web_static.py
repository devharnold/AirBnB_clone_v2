#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
"""
from datetime import datetime
from fabric.api import env, put, run, local
from os.path import exists
from os import path

env.hosts = ['35.174.185.198', '52.201.167.109']

def do_pack():
    """
    generates a .tgz archive from the contents of the web_static folder
    """
    if not exists("versions"):
        local("mkdir -p versions")

    time_format = "%Y%m%d%H%M%S"
    archive_name = "web_static_{}.tgz".format(datetime.utcnow().strftime(time_format))
    
    result = local("tar -cvzf versions/{} web_static".format(archive_name))
    if result.failed:
        return None
    else:
        return "versions/{}".format(archive_name)


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