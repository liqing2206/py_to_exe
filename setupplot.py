from cx_Freeze import setup, Executable
import os.path
import matplotlib
import matplotlib.backends.backend_tkagg

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

include_files = [os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
		 os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),(matplotlib.get_data_path(), "mpl-data")]

build_exe_options={"packages": ["tkinter", "numpy.core._methods", "numpy"],
"includes": ["numpy.core._methods", "numpy", "tkinter","matplotlib.backends.backend_tkagg"],'include_files': include_files}
		 
		 
setup(
    name='request',
    description='request',
    version='1.0',
    options={'build_exe':build_exe_options },
    executables=[Executable('request.py',
			    targetName='Schedule_request.exe',
			    copyright='Copyright (C) Cindy Li 2019',
			    base='Win32GUI')])

# python setupplot.py build
# pip install setuptools==19.2