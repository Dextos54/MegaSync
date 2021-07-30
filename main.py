import os

def platform_presets():
    if os.name == "posix":
        config_directory = "/home/{}/.config/megasync/".format(os.getlogin())
    elif os.name == "nt":
        config_directory = "C:\\Users\\{}\\AppData\\Local\\MegaSync".format(os.getlogin())