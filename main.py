from phe import paillier as pl
import numpy as np

class Server():
	def __init__(self):
		self.weight = np.array([[3,2,1],[1,3,2],[2,3,1]])
		self.studentList = []
		self.resultList = []
		

	def setList(self,list):
		self.studentList.append(list)

	def judge(self):
		for i in range(len(self.studentList)):
			self.resultList.append(np.dot(self.weight,self.studentList[i]))

class User():
	def __init__(self,name):
		self.pk, self.sk = pl.generate_paillier_keypair(n_length=256)
		self.name = name
		self.score = []
		self.encScore = []
		self.decScore = []
		self.resultScore = []
		self.subList = ["プログラマー","暗号学者","データサイエンティスト"]


	def setScore(self,seiseki1,seiseki2,seiseki3):
		print("生徒"+self.name+"の評価")
		self.score.append(seiseki1)
		print("プログラミングの成績："+str(seiseki1))
		self.score.append(seiseki2)
		print("数学の成績："+str(seiseki2))
		self.score.append(seiseki3)
		print("専門科目の成績："+str(seiseki3)+"\n")


	def encList(self):
		for i in range(len(self.score)):
			self.encScore.append(self.pk.encrypt(self.score[i]))

	def decList(self,list):
		for i in range(len(list)):
			self.resultScore.append(self.sk.decrypt(list[i]))

	def recSub(self):
		print(self.resultScore)
		print(self.name+"さんは"+self.subList[np.argmax(self.resultScore)]+"がおすすめです！\n")


def main():

	server = Server()

	A = User("A")
	B = User("B")
	C = User("C")

	A.setScore(4,2,1)
	B.setScore(1,4,3)
	C.setScore(2,4,1)

	A.encList()
	B.encList()
	C.encList()

	server.setList(A.encScore)
	server.setList(B.encScore)
	server.setList(C.encScore)

	server.judge()

	A.decList(server.resultList[0])
	B.decList(server.resultList[1])
	C.decList(server.resultList[2])

	A.recSub()
	B.recSub()
	C.recSub()

	print(server.studentList,server.resultList)



if __name__ == '__main__':
	main()