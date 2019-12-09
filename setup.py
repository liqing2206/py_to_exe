from cx_Freeze import setup, Executable
import os.path

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

include_files = [os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
		 os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll')]

setup(
    name='request',
    description='request',
    version='2.0',
    options={'build_exe': {'include_files': include_files}},
    executables=[Executable('request.py',
			    targetName='Schedule_request.exe',
			    copyright='Copyright (C) Cindy Li 2019',
			    base='Win32GUI')])

# python setup.py build
# pip install setuptools==19.2