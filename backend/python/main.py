import concurrent.futures as cf

def task(x):
    return x * x

# IO
with cf.ThreadPoolExecutor(max_workers=4) as executor:
    result = list(map(task, range(1, 9)))
    print(result)

# CPU
with cf.ProcessPoolExecutor(max_workers=4) as executor:
    result = list(map(task, range(1, 9)))
    print(result)