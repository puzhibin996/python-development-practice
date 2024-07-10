from myWorkerThread import WorkerThread

# 多线程返回执行结果
def callback(result):
    print('线程返回结果：%d' % result)

print('线程运行。。。。')

worker = WorkerThread(callback)
worker.start()
worker.join()
print('程序结束。。。。')
