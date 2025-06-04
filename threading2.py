import threading
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

start_time = time.time()
threads = []
ranges = [(0, 100000), (100000, 200000), (200000, 300000), (300000, 400000)]

for r in ranges:
    t = threading.Thread(target=count_primes, args=r)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end_time = time.time()
print(f"Total time (Threading, CPU-bound): {end_time - start_time:.2f} seconds")
