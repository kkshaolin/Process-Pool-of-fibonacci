import multiprocessing
import time

def fibonacci(n):
    number =[0,1]
    for i in range(2,n):
        number.append(number[i-1]+number[i-2])
    return number

def multi(n):
    with multiprocessing.Pool() as pool:
        pool.map(fibonacci, [n])

if __name__ == "__main__":
    n = 10**5
    print("Starting calculation")
    start = time.time()
    multi(n)
    duration = time.time() - start
    print(f"Duration {duration} seconds")