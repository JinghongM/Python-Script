def test(testname,char1,char2):
	fh=open(testname+'.txt')
	fh1=open("newtest"+'.txt','w')
	for line in fh:
		line=line.replace(char1,char2)
		print line
		fh1.write(line)
	fh1.close
