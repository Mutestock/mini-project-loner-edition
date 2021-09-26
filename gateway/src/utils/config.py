import os
import toml

_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
_ROOT_DIR = os.path.dirname(_ROOT_DIR)

ROOT_DIR = os.path.dirname(_ROOT_DIR)
CONFIG_FILE_PATH = ROOT_DIR + "/config.toml"
CONFIG = {}
DATABASE_CONFIG = {}

_filename = CONFIG_FILE_PATH
_content: str = ""

with open(_filename) as f:
    _content = f.read()
    
CONFIG = toml.loads(_content)
if os.getenv("CONTAINERIZED", None):
    DATABASE_CONFIG = CONFIG["containerized"]["database"]
else:
    DATABASE_CONFIG = CONFIG["development"]["database"]
    
