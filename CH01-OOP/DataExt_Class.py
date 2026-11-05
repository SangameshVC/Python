import sys
print(sys.executable)  #to see which interpreter we are using

import pandas as pd

class MyClass:
    
    def __init__(self,path):
        self.path=path
    
    def fetch_text(self,separator):
        df=pd.read_csv(self.path, sep=separator)
        print(df.head())
        
    def fetch_json(self):
        df=pd.read_json(self.path)
        print(df.head())
        
    def fetch_parquet(self):
        df=pd.read_parquet(self.path)
        print(df.head())
        
obj1=MyClass('CH01-OOP\Files\orders.csv')
obj1.fetch_text(',')

obj2=MyClass('CH01-OOP\Files\orders.tsv')
obj2.fetch_text('\t')

obj3=MyClass('CH01-OOP\Files\orders.json')
obj3.fetch_json()

obj4=MyClass('CH01-OOP\Files\orders.parquet')
obj4.fetch_parquet()



