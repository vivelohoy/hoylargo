from tools.fablib import *
import os

"""
Base configuration
"""
env.project_name = 'hoylargo'
env.file_path = '.'

"""
Add HipChat info to send a message to a room when new code has been deployed.
"""
env.hipchat_token = os.environ.get('HIPCHAT_ACCESS_TOKEN', '')
env.hipchat_room_id = os.environ.get('HIPCHAT_ROOM_ID', '')

# Environments
def production():
    """
    Work on production environment
    """
    env.settings = 'production'
    env.hosts = [os.environ['WPENGINE_DEVPROD_HOST']]
    env.user = os.environ['WPENGINE_DEVPROD_USERNAME']
    env.password = os.environ['WPENGINE_DEVPROD_PASSWORD']


def staging():
    """
    Work on staging environment
    """
    env.settings = 'staging'
    env.hosts = [os.environ['WPENGINE_DEVSTAGING_HOST']]
    env.user = os.environ['WPENGINE_DEVSTAGING_USERNAME']
    env.password = os.environ['WPENGINE_DEVSTAGING_PASSWORD']

try:
    from local_fabfile import  *
except ImportError:
    pass
