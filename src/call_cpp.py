import cffi
import os
from pathlib import Path

NAME = './sql.so'
PATH = str(Path.cwd()) + "/db/demo.db"
if "src" not in str(Path.cwd()):
    NAME = './src/' + NAME.replace('./','')
    PATH = str(Path.cwd()) + "/src/db/demo.db"

ffi = cffi.FFI()
ffi.cdef("""
    int cffi_insert_database(const char path[],int id,const char name[],int age,const char address[],int salary);
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
    # name_arr = []
    # name_arr += [target_list for target_list in name]
    # address_arr = []
    # address_arr += [target_list for target_list in address]

    tmp = C.cffi_insert_database(PATH.encode('ascii'),id,name.encode('ascii'),age,address.encode('ascii'),salary)
    print("Call c function success {0}".format(tmp))


