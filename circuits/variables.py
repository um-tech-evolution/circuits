'''
variables.py
Shared set of boolean variables for use in all technologies.
'''


from pyeda.boolalg.bdd import bddvars


# The number of total variables that will be allocated. Set to 16 based on the
# requirements found in [1] W. Arthur and W. Polak, “The evolution of
# technology within a simple computer model,” Complexity, vol. 11, no. 5, pp.
# 23–31, 2006.
N = 16


X = bddvars('x', N)
