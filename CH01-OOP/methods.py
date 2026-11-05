class MyClass:
    
    my_var = 100
    
    #Dunder or magic method
    def __init__(self):
        print("This is constructor method")
    
    #Dunder or magic method
    def __str__(self):
        print("This is string representation method")
        
    #Instance method
    def instance_method(self):
        print("THis is instance method")
        
    @classmethod
    def _change_value(cls,new_value):
        cls.my_var=new_value
        
    @staticmethod
    def dummy(self):
        print("This is independent of class and class variables")  #we placed this function in this class to bundle related functions, that's it
        

obj1=MyClass()
print(obj1.my_var)     #output=100
obj1.instance_method()

obj1._change_value(200)
print(obj1.my_var)     #output=200

#Now I create new object and the my_var should be updated for this object too
obj2=MyClass()
print(obj2.my_var)