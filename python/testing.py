import subprocess
import sys

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import pyautogui
except ImportError:
    install_package("pyautogui")
    import pyautogui