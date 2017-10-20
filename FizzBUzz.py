class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result=[]
        for num in range(n+1):
            if num%3==0 and num%5==0:
                result.append('FizzBuzz')
            elif num%3==0:
                result.append('Fizz')
            elif num%5==0:
                result.append('Buzz')
            else:
                result.append(num)
        print result[1:]
	return result[1:]
a=Solution()
a.fizzBuzz(1)
