import os
import jangopath

path = jangopath.MODULE_PATH + "/music_helper.py"

os.system("pkill -1 -f " + path) 
