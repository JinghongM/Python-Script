def wordPattern(pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        dictionary={}
        str1=list(pattern)
        str2=list(str.split(' '))
        num=0
        if len(str1)!=len(str2):
            return False
        while num<len(str1):
            if str1[num] not in dictionary:
                dictionary[str1[num]]=str2[num]
                num+=1
				 print 'abc'
				#"add %s,%s in dictionary" %(str1[num],str2[num])
            else:
                if str2[num]==dictionary[str1[num]]:
                    num+=1
                else:
                    return False
        return True

print(wordPattern("abba","dog dog dog dog"))