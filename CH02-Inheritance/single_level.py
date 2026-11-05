class company:
    
    var="Parent_var"
    
    def __init__(self,company_name):
        self.company_name=company_name
        
    def company_info(self):
        print("Company name:",self.company_name)
        return self.company_name
    
class employee(company):
    
    def __init__(self,emp_name,company_name):
        self.emp_name=emp_name
        self.company_name=company_name
        
    def emp_info(self):
        response=company.company_info(self)         #or response=super().company_info()  --here don't pass self
        print(f"Employee {self.emp_name} works at {response}")
        print(super().var)     #printing parent class variable
        
emp_obj=employee("Sangamesh","Cognizant")
emp_obj.company_info()         #Company name: Cognizant

emp_obj.emp_info()            #Employee Sangamesh works at Cognizant

        