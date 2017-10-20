class test():
	def __init__(self):
		self.result=[]
	def addnum(self,num):
		self.result.append(num)
		print self.result
t1=test()
t1.addnum(2)
t2=test()
t2.addnum(3)