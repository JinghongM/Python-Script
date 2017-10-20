#get divisor
result,num=[],100
div=2
while div*div<=num:
	if num%div==0:
		result.append(div)
		if div*div!=num:
			result.append(num/div)
	div+=1

	