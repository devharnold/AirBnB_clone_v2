#!/usr/bin/python3
"""
Write a Fabric script that generates a .tgz archive from the contents of the 
web_static folder of your AirBnB Clone repo, using the function do_pack.
"""
import os
from fabric.api import local
from datetime import datetime
import fabric

def do_pack():
    """
    generates a .tgz archive from the contents of the web_static folder
    """
    if not os.path.exists("versions"):
        local("mkdir -p versions")

    time_format = "%Y%m%d%H%M%S"
    archive_name = "web_static_{}.tgz".format(datetime.utcnow().strftime(time_format))
    
    result = local("tar -cvzf versions/{} web_static".format(archive_name))
    if result.failed:
        return None
    else:
        return os.path.join("versions", archive_name)


