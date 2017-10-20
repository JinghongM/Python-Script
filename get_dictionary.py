#quickly get dictionray
s='abcccdadfda'
dict={}
for position,string in enumerate(s):
	dict[string]=dict.get(string,[])+[position]
print dict