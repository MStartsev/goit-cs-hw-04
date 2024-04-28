import threading
import multiprocessing
from multiprocessing import Manager

def execute_and_store_results(target_function, files, keywords, results):
    result = target_function(files, keywords)
    results.append(result)

def execute_parallel(target_function, files, keywords, parallel_type):
    try:
        manager = Manager()
        results = manager.list()
        parallel_workers = []

        if parallel_type == 'thread':
            ParallelClass = threading.Thread
        elif parallel_type == 'process':
            ParallelClass = multiprocessing.Process

        num_workers = min(8, len(files))
        chunk_size = len(files) // num_workers

        for i in range(num_workers):
            start = i * chunk_size
            end = start + chunk_size if i < num_workers - 1 else len(files)
            worker = ParallelClass(target=execute_and_store_results, args=(target_function, files[start:end], keywords, results))
            parallel_workers.append(worker)
            worker.start()

        for worker in parallel_workers:
            worker.join()

        return list(results)

    except Exception as e:
        print(f"Error: {e}")