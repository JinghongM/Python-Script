import os
import glob
fh1=open("test"+'.txt','w')
path='C:\Users\jingh\Desktop\result.2.6_rtmp\result.2.6_rtmp'
for filename in glob.glob(os.path.join(path,'*.proc')):
	if os.stat(filename).st_size==0:
		fh1.write("viewer number: "+filename[filename.find('v')+1:filename.find('v')+3] +\
		" time interval: "+filename[filename.find('t')+1:filename.find('t')+4]+" try time: ")
		if filename[filename.find('.proc')-2]=='.':
			fh1.write(filename[filename.find('.proc')-1]+' is empty')
			fh1.write('\n')
		else:
			fh1.write(filename[filename.find('.proc')-2]+filename[filename.find('.proc')-1]+' is empty')
			fh1.write('\n')
	else:
		fh1.write("viewer number: "+filename[filename.find('v')+1:filename.find('v')+3] +\
		" time interval: "+filename[filename.find('t')+1:filename.find('t')+4])
		fh1.write('\n')
		fh=open(filename)
		for line in fh:
			if len(line)>30:
				
				fh1.write(line)
				fh1.write('\n')
fh1.close