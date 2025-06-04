# cpu_threads.py
import threading
import time

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_primes(start, end):
    count = 0
    for i in range(start, end):
        if is_prime(i):
            count += 1
    print(f"Primes between {start}-{end}: {count}")

start = time.time()

threads = []
ranges = [(10_000, 50_000), (50_001, 90_000), (90_001, 130_000), (130_001, 170_000)]
for r in ranges:
    t = threading.Thread(target=count_primes, args=r)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print(f"Total time with threads: {time.time() - start:.2f} seconds")
