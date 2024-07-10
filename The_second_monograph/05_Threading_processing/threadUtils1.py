import threading
from time import sleep,ctime






#第二种方式是，我们通过继承Thread类，并运行Thread类中的init()方法来获取父类属性，并重写run()方法。在线程启动后，程序将自动执行run()方法


loops = (4,2)
class MyThread(threading.Thread):
    def __init__(self,target,args):
        super().__init__()
        self.target = target
        self.args = args
    def run(self):
        self.target(*self.args)

def loop(nloop,nsec):
    print(ctime(),'start loop',nloop)
    sleep(nsec)
    print(ctime(),'end loop',nloop)
def main():
    threads = []
    nloops = range(len(loops))
    for i in nloops:
        t = MyThread(loop,(i,loops[i],))
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()

if __name__ == '__main__':
    main()
