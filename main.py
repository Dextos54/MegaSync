import os
import argparse

def platform_presets():
    if os.name == "posix":
        config = "/home/{}/.config/megasync/".format(os.getlogin())
    elif os.name == "nt":
        config = "C:\\Users\\{}\\AppData\\Local\\MegaSync\\".format(os.getlogin())
    return config

def add_pair(config): # adds pair
    pass

# main code

parser = argparse.ArgumentParser(description='MegaSync') # arguments parser

parser.add_argument("-a", action="store_true", help="Add new pairs of folders")
config = platform_presets()
args = parser.parse_args()
if args.a:
    add_pair()



