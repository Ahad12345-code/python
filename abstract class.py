from abc import ABC, abstractmethod
# Create base class
class Absclass(ABC):
    # Function to print a value
    def print(self,x):
        print("passed value: ", x)
    # Abstract Method 
    @abstractmethod
    def task(self):
        print("We are inside ABsclass task")
# Create sub class
class test_class(Absclass):
    def task(self):
            print("We are inside test_class task")
    # object of test_class created
testobj = test_class()
testobj.task()
testobj.print(100)       
    
    