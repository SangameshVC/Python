def my_decorator(fun):
    def wrapper(*args,**kwargs):
        print("Before function")
        response=fun(*args)
        print("After function")
        return response
    return wrapper

#calling or applying decorator
@my_decorator
def fetch_data(url,path):
    return f"Fetching data from {url} and saving it to {path}"

response=fetch_data("https://example.com/data","/tmp/data.csv")
print(response)

#one more method to call or apply decorator is
def sample(a,b):
    return a,b 

res=my_decorator(sample)
response2=res(2,3)
print(response2)