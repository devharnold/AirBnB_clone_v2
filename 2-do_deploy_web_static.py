#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
"""
from datetime import datetime
from fabric.api import env, put, run, local
from os.path import exists

env.hosts = ['35.174.185.198', '52.201.167.109']

def do_deploy(archive_path):
    if not exists(archive_path):
        return False
    
    try:
        put(archive_path, '/tmp')

        archive_filename = archive_path.split('/')[-1]
        release_folder = '/data/web_static/releases/{}'.format(archive_filename.split('.')[0])
        run('mkdir -p {}'.format(release_folder))
        run('tar -xzf /tmp/{} -C {}'.format(archive_filename, release_folder))
        run('rm /tmp/{}'.format(archive_filename))
        run('mv {}/web_static/* {}'.format(release_folder, release_folder))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(release_folder))

        print("Deploy a new one!")
        
    except Exception as e:
        print("Deploy fail!:", str(e))
        return False
