#parent class
class company:
    
    var="Parent_var"
    
    def __init__(self,company_name):
        self.company_name=company_name
        
    def company_info(self):
        print("Company name:",self.company_name)
        return self.company_name

#child class
class employee(company):
    
    def __init__(self,emp_name,company_name):
        self.emp_name=emp_name
        self.company_name=company_name
        
    def emp_info(self):
        response=company.company_info(self)         #or response=super().company_info()  --here don't pass self
        print(f"Employee {self.emp_name} works at {response}")

#child class
class contractor(company):
    
    def __init__(self,contractor_name,company_name):
        self.contractor_name=contractor_name
        self.company_name=company_name
            
    def contractor_info(self):
        response=company.company_info(self)         #or response=super().company_info()  --here don't pass self
        print(f"Employee {self.contractor_name} works at {response}")



#object for employee       
emp_obj=employee("Sangamesh","Cognizant")
emp_obj.company_info()         #Company name: Cognizant
emp_obj.emp_info()            #Employee Sangamesh works at Cognizant

#object for contractor
contract_obj=contractor("Pradeep","Cognizant")
contract_obj.contractor_info()        