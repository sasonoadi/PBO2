print("Program to demonstrate to handle ImportError:")
print("\n")
try:
from crypt import pwd
except ImportError as ie:
print("It cannot import module and submodule", ie)