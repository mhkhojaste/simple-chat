import ctypes
import socket
import threading
import time

# this class is used for send broadcast
class thread_with_exception(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        try:
            i = 0
            server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
            server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            server.settimeout(0.2)
            server.bind(("", 44444))
            message = b"is there any one ?" + b"127.0.0.1," + b"5005"
            while True:
                server.sendto(message, ('<broadcast>', 37020))
                print("Is there any one?")
                time.sleep(1)
                i += 1
        finally:
            print()

    def get_id(self):
        if hasattr(self, '_thread_id'):
            return self._thread_id
        for id, thread in threading._active.items():
            if thread is self:
                return id

    def raise_exception(self):
        thread_id = self.get_id()
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
                                                         ctypes.py_object(SystemExit))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
            print('Exception raise failure')
