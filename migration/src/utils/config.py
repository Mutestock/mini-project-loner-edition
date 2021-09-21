import os
from .aliases import ROOT_DIR
import toml

CONFIG_FILE_PATH = ROOT_DIR + "/config.toml"

filename = "file.py"
content = ""

with open(filename) as f:
    content = f.readlines()

# Switches depending on whether or not the project is containerized.
# This is for manual execution versus containerized execution.
