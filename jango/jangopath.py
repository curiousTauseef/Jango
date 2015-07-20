import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
HOME_DIR = os.environ['HOME']

MODULE_PATH = os.path.join(BASE_DIR, 'jango')  
CONFIG_PATH = os.path.join(HOME_DIR, '.Jango_config.cfg')
TEXT_PATH = os.path.join(HOME_DIR, '.Jango_data.txt')
