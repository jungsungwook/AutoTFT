import sys
from cx_Freeze import setup, Executable
 
##build_exe_options = dict(
##        compressed = True,
##        includes = ["cv2","time","keyboard","tkinter","multiprocessing", "pyautogui","PIL","ctypes"],
##        include_files = []
##)
## 

setup(
    name = "testSetup",
    version = "1.0",
    author="jswcyber",
    description = "1.0V",
    executables = [Executable("test.py")]
)
