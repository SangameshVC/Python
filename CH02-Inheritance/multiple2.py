class company:
    
    def __init__(self,company_name):
        self.company_name=company_name
        
    def info(self):
        return self.company_name
    
class client_company:
    def __init__(self,client_name):
        self.client_name=client_name
        
    def info(self):
        return self.client_name
    
class employee(company,client_company):
    def __init__(self,employee_name,company_name,client_name):
        self.employee_name=employee_name
        self.company_name=company_name
        self.client_name=client_name
        
    def info(self):
        response1=company.info(self)
        response2=client_company.info(self)
        print(f"Employee {self.employee_name} works at {response1} for project {response2}")
        
obj=employee("Sangamesh","Cognizant","TDECU")
obj.info()