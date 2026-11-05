#Withoud threading
import time

def fetch_data(url):
    print("Fetching data from ",url)
    time.sleep(5)
    print("Data fetched from ",url)
    return "Data from " + url

url_list=["url1","url2","url3","url4","url5"]
for i in url_list:
    fetch_data(i)