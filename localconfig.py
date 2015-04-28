# This is for testing localconfig import bugs that happened with the Python 3
# compatibility patch. It'll be automatically included with tests and cause
# regressions if there are any.
from pyconfig import Namespace

conf = Namespace({'inp1':True, 'inp2':False})
conf.local = True
conf.inp2 = True # overriding
