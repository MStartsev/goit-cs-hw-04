# main.py
from file_search.execute_parallel import execute_parallel
from file_search.search_files import search_files, search_files_sequential
import time
import os
import random
from faker import Faker

def main():
    directory = "library/"
    files = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f.endswith('.txt')]
    
    # file generator
    fake = Faker()
    os.makedirs(directory, exist_ok=True)

    for i in range(1000):
        file_name = os.path.join(directory, f"file_{i}.txt")
        with open(file_name, "w", encoding="utf-8") as f:
            for _ in range(10000):
                f.write(fake.text())

    # Create a list of unique keywords
    keywords = list(set([fake.word() for _ in range(4)]))
    # keywords = ['above', 'machine', 'defense','random']
    
    # Sequential approach
    start_time = time.time()
    sequential_results = search_files_sequential(files, keywords)
    sequential_time = time.time() - start_time

    # Threading approach
    start_time = time.time()
    threading_results = execute_parallel(search_files, files, keywords, 'thread')
    threading_time = time.time() - start_time

    # Multiprocessing approach
    start_time = time.time()
    multiprocessing_results = execute_parallel(search_files, files, keywords, 'process')
    multiprocessing_time = time.time() - start_time

    print("Sequential results:", sequential_results)
    print("Threading results:", threading_results)
    print("Multiprocessing results:", multiprocessing_results)
    print("Sequential time:", sequential_time)
    print("Threading time:", threading_time)
    print("Multiprocessing time:", multiprocessing_time)

if __name__ == "__main__":
    main()
