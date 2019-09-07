import socket

HOST = b"127.0.0.1,"
PORT = b"65432"
Message = b"I am here!"
HOST_st = "127.0.0.1"
PORT_int = 65432
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
client.bind(("", 37020))

# receive a broadcast message
while True:
    data, addr = client.recvfrom(1024)
    print("received message: %s" % data)
    st = str(data)
    sock = socket.socket(socket.AF_INET,
                         socket.SOCK_DGRAM)
    sock.sendto(Message + HOST + PORT, (st[st.index("?") + 1: st.index(",")], int(st[st.index(",") + 1:len(st) - 1])))
    break

# open a tcp connection for chat, end chat when enter end
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST_st, PORT_int))
    s.listen(1)
    conn, addr_tcp = s.accept()
    with conn:
        print("connected ")
        while True:
            data2 = conn.recv(1024)
            str_data = str(data2)
            if str_data[str_data.index("'") + 1: str_data.rindex("'")] == "end":
                print("chat ended!")
                conn.sendall("end".encode("UTF-8"))
                s.close()
                break
            print("Received message : ", str_data[str_data.index("'") + 1: str_data.rindex("'")])
            data = input("Enter your message : ")
            conn.sendall(data.encode("UTF-8"))
            if data == "end":
                print("chat ended!")
                s.close()
                break









