import numpy as np
import socket
import pickle
HOST = '127.0.0.1'
PORT = 50000

class Server():
    def __init__(self):
        self.weight = np.array([[3,2,1],[1,3,2],[2,3,1]])

    def setList(self,list):
        self.studentList = list
        print(self.studentList)

    def judge(self):
        self.resultList = np.dot(self.weight,self.studentList)

def main():

    server = Server()
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    s.bind((HOST, PORT))

    while True:
        s.listen()

        client, _ = s.accept()
        recv_data = client.recv(2048)
        recv_data = pickle.loads(recv_data)

        server.setList(recv_data)

        print("以下のデータをユーザから受信しました\n")
        print("---------------------------------------------")
        print(server.studentList)
        print("---------------------------------------------\n")

        server.judge()

        print("以下のデータをユーザへ送信します\n")
        print("---------------------------------------------")
        print(server.resultList)
        print("---------------------------------------------\n")  

        send_data = pickle.dumps(server.resultList)
        client.send(send_data)

    client.close()

if __name__ == '__main__':
    main()