import multiprocessing
import time

def download_file(file_id):

    print(f"Downloaded file {file_id}")

if __name__ == '__main__':
    start_time = time.time()
    processes = []

    for i in range(4):
        p = multiprocessing.Process(target=download_file, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    end_time = time.time()
    print(f"Total time (Multiprocessing, I/O-bound): {end_time - start_time:.2f} seconds")
