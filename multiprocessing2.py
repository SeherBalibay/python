import multiprocessing
import time

def count_primes(start, end):
    primes = []
    for num in range(start, end):
        if num < 2:
            continue
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            primes.append(num)

if __name__ == '__main__':
    start_time = time.time()
    processes = []
    ranges = [(0, 100000), (100000, 200000), (200000, 300000), (300000, 400000)]

    for r in ranges:
        p = multiprocessing.Process(target=count_primes, args=r)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    end_time = time.time()
    print(f"Total time (Multiprocessing, CPU-bound): {end_time - start_time:.2f} seconds")
