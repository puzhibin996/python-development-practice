import threading
import time


class WorkerThread(threading.Thread):
    def __init__(self, callback):
        super(WorkerThread, self).__init__()
        self.callback = callback

    def run(self):
        time.sleep(5)
        self.callback(5)
