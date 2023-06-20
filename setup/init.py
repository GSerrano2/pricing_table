import os
import platform
from variables import env

def updateRequirements():
    if not(os.path.exists(env.ENV_FOLDER) and os.path.isdir(env.ENV_FOLDER)):
        os.system(env.ENV_SETUP)
        system = checkOS()
        print('System:', system)
        if system == 'Windows':
            os.system(rf'{getAbsPath()}{env.ENV_ACTIVATE_WIN}')
        else:
            os.system(rf'{getAbsPath()}{env.ENV_ACTIVATE}')
        os.system(env.ENV_INSTALL)
    return

def checkOS():
    return platform.system()

def getAbsPath():
    abs_path = os.path.abspath("main.py")
    last_slash = abs_path.rfind('\\')
    abs_path = abs_path[:last_slash]
    return abs_path