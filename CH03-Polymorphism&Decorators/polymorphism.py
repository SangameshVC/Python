class api_fetch:
    def fetch(self):
        print("Fetching data from API...")
        
class db_fetch:
    def fetch(self):
        print("Fetching data from database....")
        
class s3_fetch:
    def fetch(self):
        print("Fetching data from S3bucket....")
        

#method fetch() remains same, but it's functionality depends on object
obj1=api_fetch()
obj1.fetch()                 #Fetching data from API...

obj2=db_fetch()
obj2.fetch()                 #Fetching data from database....

obj3=s3_fetch()
obj3.fetch()                #Fetching data from S3bucket....