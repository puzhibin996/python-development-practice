from concurrent.futures import ThreadPoolExecutor
import os,time,random


def task(n):
    print(f"子线程：{os.getpid()}正在执行")
    time.sleep(random.randint(1,3))
    return n**2

def result_back(res):
    print(res.result())

if __name__ == '__main__':
    thread_pool = ThreadPoolExecutor(max_workers=4)
    for i in range(1,10):
        future = thread_pool.submit(task,i)
        future.add_done_callback(result_back)
    thread_pool.shutdown(True)
