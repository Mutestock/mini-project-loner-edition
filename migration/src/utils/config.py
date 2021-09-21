import os
import toml

_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
_ROOT_DIR = os.path.dirname(_ROOT_DIR)
ROOT_DIR = os.path.dirname(_ROOT_DIR)

CONFIG_FILE_PATH = ROOT_DIR + "/config.toml"

filename = CONFIG_FILE_PATH
content: str = ""

with open(filename) as f:
    content = f.read()
    
    
CONFIG = toml.loads(content)
MIGRATIONS_FOLDER_PATH = ROOT_DIR + CONFIG["misc"]["migrations_folder"]



