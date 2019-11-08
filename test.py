import tkinter as tk

class Application(tk.Frame):
	def __init__(self,master):
		super().__init__(master)
		self.pack()

		# master.geometry("300x300")
		# master.title("Server")
		# self.master.config(bg="black")

		self.window = []
		self.user = []

		for i in ["A","B","C"]:
			self.window.append(tk.Toplevel())
			self.user.append(User(self.window[len(self.window)-1],i))

		self.label = tkinter.Label(text='プログラミングの評価')
		self.label.place(x=30, y=70)
		self.label = tkinter.Label(text='数学の評価')
		self.label = tkinter.Label(text='専門科目の評価')
		self.button = tk.Button(master,text="クリック",command=self.buttonClick,width=10)
		self.button.place(x=110, y=180)

	def buttonClick(self):
		print("サーバだよ！")

class User(tk.Frame):
	def __init__(self,master,name):
		super().__init__(master)
		self.pack()

		self.name = name

		master.geometry("300x300")
		master.title("ユーザ"+self.name)

		self.button = tk.Button(master,text="クリック",command=self.buttonClick,width=10)
		self.button.place(x=110, y=180)

	def buttonClick(self):
		print("押した"+self.name)


def main():
	win = tk.Tk()

	app = Application(win)

	app.mainloop()



if __name__ == "__main__":
	main()