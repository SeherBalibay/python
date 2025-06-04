import threading
import requests
import time


URLS = ["https://httpbin.org/delay/1"] *3

def fetch_url(url):

       response = requests.get(url)
       print(f"{url} - Status: {response.status_code}")


def main():
    threads = []
    start_time = time.time()

    for url in URLS:
        thread = threading.Thread(target=fetch_url, args=(url,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"Threading took {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()
