import multiprocessing
import concurrent.futures
import time

def fibonacci(n):
    num = [0, 1]
    for i in range(2, n):
        num.append(num[i-1] + num[i-2])
    return num

def multi(n):
    with multiprocessing.Pool() as pool:
        pool.map(fibonacci, n) 

def synchronous(n):
    num = []
    for i in n:
        num.append(fibonacci(i))
    return num

def threaded(n):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(fibonacci, n)

if __name__ == "__main__":
    n = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print("Starting calculation")
    start_multi = time.time()
    multi_results = threaded(n)
    duration_multi = time.time() - start_multi
    print(f"Multiprocessing Duration: {duration_multi} seconds")