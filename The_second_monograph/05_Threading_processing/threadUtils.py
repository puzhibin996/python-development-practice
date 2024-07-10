
from threading import Thread,currentThread
from time import sleep

# 第一种方式是，我们通过创建Thread的实例，并传递一个函数
def fun_thread(sec,tname):
    print("启动线程",currentThread().getName(),":",currentThread().is_alive())
    print("线程名称：",tname,"线程编号：",sec)
    print("setName 修改线程名称")
    currentThread().setName(tname)
    sleep(sec)
    print("{}线程结束".format(currentThread().getName()))


if __name__ == "__main__":
    threads = [] # 维护线程
    for i in range(3):
        t = Thread(target=fun_thread,name="thread-%d"%i,
                   args=(3,"My"+str(i)+"Thread"))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()