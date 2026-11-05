import time
from concurrent.futures import ThreadPoolExecutor

def fetch_data(url):
    print("Fetching data from ",url)
    time.sleep(5)
    print("Data fetched from ",url)
    return "Data from " + url

url_list=["url1","url2","url3","url4","url5"]
    
results=[]

with ThreadPoolExecutor(max_workers=len(url_list)) as executor:
    futures = executor.map(fetch_data,url_list)
    results.extend(futures)
    
print(results)