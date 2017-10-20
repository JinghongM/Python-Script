nums=[1,2,3,4,5]
i=0
dict={}
while i<len(nums)-1:
	j=i+1
	while j<len(nums):
		num=nums[i]+nums[j]
		dict.setdefault(num,[])
		print nums[i],nums[j]
		dict[num].append(str(nums[i])+' '+str(nums[j]))
		j+=1
	i+=1
print dict