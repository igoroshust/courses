import time
import requests


# I/O
def fetch_url(url):
    r = requests.get(url)
    return r.text


# CPU
def heavy_compute(n):
    total = 0
    for i in range(n):
        total += i**2
    return total


start = time.time()
fetch_url('https://jsonplaceholder.typicode.com/users/1/')
print('IO: ', time.time() - start)
        
start = time.time()
heavy_compute(10_000_000)
print('CPU: ', time.time() - start)
        