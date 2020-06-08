def to_base(num,base):
	'''
	converts a number in base 10 to a number in base 2,4,8 or 16 
	'''
	assert type(num)==int and type(base)==int and base in set([2,4,8,16])
	n=base-1
	shift=1 #detrmines by how many bits we are going to shift after aech iteration
	while 2**shift<base:
		shift+=1
	ans=''
	while num:
		x=num&n
		x=str(x) if x<10 else chr(ord('A')+x-10)#in case of base 16
		ans=x+ans
		num=num>>shift#number shifts by the value f bits
	return ans if len(ans)>0 else 0

#to test 	
#print(to_base(665,16)) #returns 299
