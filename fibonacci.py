import time

def fibonacci(n):
    num = [0, 1]
    for i in range(2, n):
        num.append(num[i-1] + num[i-2])
    return num

def synchronous(n):
    num = []
    for i in n:
        num.append(fibonacci(i))
    return num

if __name__ == "__main__":
    n = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print("Starting calculation")
    start_multi = time.time()
    multi_results = synchronous(n)
    duration_multi = time.time() - start_multi
    print(f"Duration: {duration_multi} seconds")