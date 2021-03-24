from .api import *
from .err import *

__version__='1.0.0'

_ltype = {0:'INFO', 1:'ERROR', 2: 'WARNING', 3: 'DEBUG', 4:'CRITICAL'}

# Exceptions
class LoggerCodeError(Exception):
	pass

class LoggerFileError(Exception):
	pass

if __name__ == '__main__':
	pass
