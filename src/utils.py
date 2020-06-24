
from src import call_cpp

class test(object):
    def __init__(self):
        print("start test class")
        self.result = 0
        
    def print_string(self,str):
        print(str)
        call_cpp.main()
        self.result = 1
        return self.result