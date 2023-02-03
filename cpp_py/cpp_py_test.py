from ctypes import *

lib = CDLL("C++/source/build/libcpp_python.dll", winmode=0)

lib.adder.restype = c_int
lib.adder.argtypes = [c_int, c_int]

arg1 = 10
arg2 = 15

res = lib.adder(arg1, arg2)

print(res)
