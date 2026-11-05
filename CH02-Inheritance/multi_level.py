#parent class
class company:
    
    var="Parent_var"
    
    def __init__(self,company_name):
        self.company_name=company_name
        
    def info(self):
        return self.company_name

#parent of employee and child of company
class manager(company):
    
    def __init__(self,manager_name,company_name):
        self.manager_name=manager_name
        self.company_name=company_name
        
    def info(self):
        response=company.info(self)
        print(f"The manager {self.manager_name} works at {self.company_name}")
        return self.manager_name

#child
class employee(manager):
    
    def __init__(self,employee_name,manager_name,company_name):
        self.employee_name=employee_name
        self.manager_name=manager_name
        self.company_name=company_name
        
    def info(self):
        response2=manager.info(self)
        print(f"The employee {self.employee_name} works under {response2} at {self.company_name}")
        
        
obj=employee("Sangamesh","Sunil","Cognizant")
obj.info()