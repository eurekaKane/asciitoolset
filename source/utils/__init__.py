from .utils import *

__local = os.getcwd()

#SHARED_DIRECTORY = os.path.join(os.environ["APPDATA"])

path_to_fnts = importlib.resources.files('pyfiglet.fonts')

FILES = f"{path_to_fnts}\\files.txt"

__tmp = f"{__local}\\tmp"