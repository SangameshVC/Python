class MyClass:
    
    var1="Sangamesh"
    var2="Chikkanagi"
    
    '''Constructor(These are used to take user inputs), When we create obj of class constructors will be called automatically,
       Hence, we pass the arguments during object creation'''
    def __init__(self,a:str,b,c):      #here a:str --> type hint
        self.a=a     #public
        self.__b=b   #private
        self._c=c    #protected
        
    def func1(self):
        print(self.a)
        
    def func2(self):
        print(self.__b)
        
    def func3(self):
        print(self._c)

obj1=MyClass("func1","func2","func3")
obj1.a= "updated func1"      #here i updated the variable a
obj1.func1()

obj1.b="updated func2"      #here when i update the vale 'b', it won't update vale of '__b'.
print(obj1.b)               #Instead it create new variable 'b' and assign that updated value to it
#print(obj1.__b)  #--> for this it throws variable bcz private variables are not accessible outside the class

obj1._c="updated func3"    #we can update the vale of protected variable outside the class and it is accessible too
obj1.func3()               #'_' id just indication that tells it is protected 


#Now I create one new object
obj2=MyClass("func1","func2","func3")
obj2.func1()                 #all the values remains original.
obj2.func2()                 #It means whatever changes we made those are specific to that object only.
obj2.func3()



