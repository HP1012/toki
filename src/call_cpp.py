import cffi
import os
from pathlib import Path

NAME = './libhello.so'
if "src" not in str(Path.cwd()):
    NAME = './src/' + NAME.replace('./','')

ffi = cffi.FFI()
ffi.cdef("""
    int cffi_sum(int a, int b);
    void cffi_hello(char* name);
    """)
try:
    C = ffi.dlopen(NAME)
except Exception as _:
    os.system('cd ./src/;make all')
    C = ffi.dlopen(NAME)

def py_sum(a,b):
    return C.cffi_sum(a,b)
def py_hello(name):
    return C.cffi_hello(name)

def main():
    tmp = py_sum(10,11)
    print("Call c function success {0}".format(tmp))


