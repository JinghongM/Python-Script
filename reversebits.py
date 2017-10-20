bit='{0:032b}'.format(135)
print bit
bit=bit[2:len(bit)]
print bit
bit=bit[::-1]
print bit
result='0b%s' %bit
print int(result,2)

