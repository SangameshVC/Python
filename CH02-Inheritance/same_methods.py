#parent class
class company:
    
    var="Parent_var"
    
    def __init__(self,company_name):
        self.company_name=company_name
        
    def info(self):
        return self.company_name

#child class
class employee(company):
    
    def __init__(self,emp_name,company_name):
        self.emp_name=emp_name
        self.company_name=company_name
        
    def info(self):
        response=company.info(self)         #or response=super().info()  --here don't pass self
        print(f"Employee {self.emp_name} works at {response}")
        
        
#object
obj=employee("Sangamesh","Cognizant")
obj.info()      #Employee Sangamesh works at Cognizant

'''
Here we have two info() methods, one in parent and one in child.
But when I created object of child and called the info() method it took child class's info() method.
Bcz there is rule like it picks closest member of object.
'''
