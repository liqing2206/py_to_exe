import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os", "sys", "PySide", "datetime", "subprocess"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

options = {
    'build_exe': {
        'includes': 'atexit'
    }
}

executables = [
    Executable('request.py', base=base)
]

setup(  name = "request",
        version = "0.1",
        description = "schedule request",
        options = options,
        executables = executables)

#python3.3 setupmac.py bdist_mac