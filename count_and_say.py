class Solution(object):
    result={1:'1'}
    def countAndSay(self, n):
		if n in Solution.result:
			return Solution.result[n]
			
		else:
			
			for i in range(2,n+1):
				self.add(i)
		return Solution.result[n]
				
    def add(self,n):
		pre=Solution.result[n-1]
		res=""
		now=pre[0]
		now_num=0
		for i in pre:
			if i==now:
				now_num=now_num+1
			else:
				res=res+str(now_num)+str(now)
				now=i
				now_num=1
		res=res+str(now_num)+str(now)
		Solution.result[n]=res

t=Solution()
print t.countAndSay(1)
print t.countAndSay(5)
