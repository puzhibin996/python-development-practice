from concurrent.futures import ThreadPoolExecutor
import os,time,random



#  使用线程池来执行线程任务的步骤如下。
# （1）调用ThreadPoolExecutor类的构造器创建一个线程池。
# （2）定义一个普通函数作为线程任务。
# （3）调用ThreadPoolExecutor对象的submit()方法来提交线程任务。
# （4）当不想提交任何任务时，调用ThreadPoolExecutor对象的shutdown()方法来关闭线程池。
def task(n):
    print(f"子线程：{os.getpid()}正在执行")
    time.sleep(random.randint(1,3))#模拟任务执行时间
    return n**2

if __name__ == '__main__':
    thread_pool = ThreadPoolExecutor(max_workers=4)# 设置线程大小
    futures = []
    for i in range(1,10):
        future = thread_pool.submit(task,i)
        futures.append(future)
    thread_pool.shutdown(True)

    for future in futures:
        print(future.result())
