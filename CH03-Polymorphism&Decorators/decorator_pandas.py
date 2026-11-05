def pandas_decorator(fx):
    
    def main_function(*args):
        result=fx(*args)
        result.to_parquet("result2.parquet")
        #r"C:\\Users\\hpd21\\OneDrive\\Desktop\\Sangamesh\\Python Advanced\\CH03-Polymorphism&Decorators\\result.parquet"
        return result
    return main_function


@pandas_decorator
def csv_to_parquet(file_path):
    import pandas as pd
    df = pd.read_csv(file_path)
    return df

obj=csv_to_parquet("orders.csv")
#r"C:\\Users\\hpd21\\OneDrive\\Desktop\\Sangamesh\\Python Advanced\\CH03-Polymorphism&Decorators\\orders.csv"
print(obj.head())