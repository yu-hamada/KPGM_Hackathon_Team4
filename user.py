from phe import paillier as pl
import numpy as np
import socket
import pickle
import tkinter as tk
import tkinter.ttk as ttk

HOST = '127.0.0.1'
PORT = 50000
N = 3
BG = 'pink'
FONT = ("メイリオ", "9", "bold")

class Application(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack()
        master.withdraw()

        self.window = []
        self.user = []

        for i in ["A","B","C"]:
            self.window.append(tk.Toplevel())
            self.user.append(User(self.window[len(self.window)-1],i))

class User(tk.Frame):
    def __init__(self,master,name):
        super().__init__(master)
        self.pack()

        self.name = name

        self.pk, self.sk = pl.generate_paillier_keypair(n_length=256)
        self.score = [0] * N
        self.encScore = [0] * N
        self.decScore = [0] * N
        self.resultScore = [0] * N
        self.subList = ["プログラマー","暗号学者","データサイエンティスト"]


        master.geometry("300x300")
        master.title("進路評価システム")
        master.config(bg=BG)

        self.lblUser = tk.Label(master, text = "【ユーザ"+self.name + "】", bg= BG, font = FONT)
        self.lblUser.place(x=20,y=10)

        self.lbl1 = tk.Label(master, width=20, text = "プログラミングの成績：", anchor='e', justify='right', bg=BG, font = FONT)
        self.lbl1.place(x=20,y=50)

        self.com1 = ttk.Combobox(master, state='readonly', width=5)
        self.com1["values"] = (1,2,3,4)
        self.com1.current(0)
        self.com1.place(x=185,y=50)

        self.lbl2 = tk.Label(master, width=20, text = "数学の成績：", anchor='e', justify='right', bg=BG, font = FONT)
        self.lbl2.place(x=20,y=80)

        self.com2 = ttk.Combobox(master, state='readonly', width=5)
        self.com2["values"] = (1,2,3,4)
        self.com2.current(0)
        self.com2.place(x=185,y=80)

        self.lbl3 = tk.Label(master, width=20, text = "専門科目の成績：", anchor='e', justify='right', bg=BG, font = FONT)
        self.lbl3.place(x=20,y=110)
    
        self.com3 = ttk.Combobox(master, state='readonly', width=5)
        self.com3["values"] = (1,2,3,4)
        self.com3.current(0)
        self.com3.place(x=185,y=110)

        self.button = tk.Button(master,text="送信",command=self.buttonClick,width=10, font = FONT)
        self.button.place(x=110, y=170)
        self.button.config(fg="black", bg="skyblue")

        self.lblDec = tk.Label(master,text = "復号結果：", bg=BG, font = FONT)
        self.lblDec.place(x=30,y=230)

        self.entDec = tk.Entry(master, width=10)
        self.entDec.place(x=30,y=260)

        self.lblJob = tk.Label(master,text = self.name+"さんのおすすめは：", bg=BG, font = FONT)
        self.lblJob.place(x=150,y=230)

        self.entJob = tk.Entry(master, width=20)
        self.entJob.place(x=150,y=260)

    def buttonClick(self):
        self.entDec.delete(0, tk.END)
        self.entJob.delete(0, tk.END)
        self.setScore(int(self.com1.get()),int(self.com2.get()),int(self.com3.get()))

        self.encList()

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((HOST, PORT))

        print(self.name + "さんの暗号化された成績データをサーバへ送信します\n")

        self.send_data = pickle.dumps(self.encScore)
        self.s.send(self.send_data)

        self.recv_data = self.s.recv(2048)
        self.recv_data = pickle.loads(self.recv_data)

        print(self.name + "さんが暗号化された判定データをサーバから受信しました\n")

        self.decList(self.recv_data)

        self.recSub()


    def setScore(self,seiseki1,seiseki2,seiseki3):
        self.score[0] = seiseki1
        self.score[1] = seiseki2
        self.score[2] = seiseki3

    def encList(self):
        for i in range(len(self.score)):
            self.encScore[i] = self.pk.encrypt(self.score[i])

    def decList(self,list):
        for i in range(len(list)):
            self.resultScore[i] = self.sk.decrypt(list[i])

    def recSub(self):
        self.entDec.insert(tk.END, self.resultScore)
        self.entJob.insert(tk.END, self.subList[np.argmax(self.resultScore)])



def main():

    win = tk.Tk()
    app = Application(win)
    app.mainloop()


if __name__ == '__main__':
    main()