class MyClass:
    
    var1="Sanagmesh"
    var2="Chikkanagi"
    
    '''Constructor(These are used to take user inputs), When we create obj of class constructors will be called automatically,
       Hence, we pass the arguments during object creation'''
    def __init__(self,a:str,b,c):      #here a:str --> type hint
        self.a=a
        self.b=b
        self.c=c
        
    def func1(self):
        print(self.a)
        
    def func2(self):
        print(self.b)
        
    def func3(self):
        print(self.c)

obj1=MyClass("func1","func2","func3")
obj1.func1()

obj2=MyClass("func1","func2","func3")
obj2.func2()

obj3=MyClass("func1","func2","func3")
obj3.func3()
