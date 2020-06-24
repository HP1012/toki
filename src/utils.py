
from src import call_cpp

class test(object):
    def __init__(self):
        print("start test class")
        self.result = 0
        
    def print_string(self,str):
        print(str)
        # call_cpp.main()
        self.result = 1
        return self.result
    def insert_database(self,data):
        call_cpp.main(int(data[0]),data[1],int(data[2]),data[3],int(data[4]))
        self.result = 1
        return self.result