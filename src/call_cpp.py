import cffi
import os
from pathlib import Path

NAME = './sql.so'
if "src" not in str(Path.cwd()):
    NAME = './src/' + NAME.replace('./','')

ffi = cffi.FFI()
ffi.cdef("""
    int cffi_insert_database(int id,const char name[],int age,const char address[],int salary);
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

def main(id,name,age,address,salary):
    name_arr = []
    name_arr += [target_list for target_list in name]
    address_arr = []
    address_arr += [target_list for target_list in address]

    tmp = C.cffi_insert_database(id,name_arr,age,address_arr,salary)
    print("Call c function success {0}".format(tmp))


