import socket
import time

# import thread for send broadcast
from ThreadServer import thread_with_exception
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
TCP_IP = ""
TCP_PORT = 0
t1 = thread_with_exception('Thread 1')
t1.start()

sock = socket.socket(socket.AF_INET,
                    socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

# listen if some client get broadcast message
while True:
    data, addr = sock.recvfrom(1024)
    print("connection find out", data)
    st = str(data)
    TCP_IP = st[st.index("!") + 1: st.index(",")]
    TCP_PORT = int(st[st.index(",") + 1:len(st) - 1])
    break
sock.close()
# when find some client close broadcast
t1.raise_exception()

# open chat with client that found, end chat when enter end
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print(TCP_IP)
    print(TCP_PORT)
    s.connect((TCP_IP, TCP_PORT))
    while True:
        data = input("Enter your message : ")
        s.sendall(data.encode("UTF-8"))
        data2 = s.recv(1024)
        str_data = str(data2)
        if str_data[str_data.index("'") + 1: str_data.rindex("'")] == "end":
            time.sleep(2)
            print("chat ended!")
            s.shutdown(socket.SHUT_RDWR)
            break
        print("Received message : ", str_data[str_data.index("'") + 1: str_data.rindex("'")])

