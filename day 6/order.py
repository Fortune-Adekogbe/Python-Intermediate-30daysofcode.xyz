def order(arr):
	'''
	returns longest consecutive numbers in a list
	'''
	s=set(arr)
	longest=0
	start=arr[0]
	for i in arr:
		if type(i)!=int:
			raise AssertionError
		if i-1 not in s:
			st=i
			length=1
			while i+1 in s:
				i+=1
				length+=1
			if longest==length:
				start=min(st,start)
			elif longest<length:
				start=st
			longest=max(longest,length)
	rem=[]
	for i in arr:
		if not(start<=i<=start+longest):
			rem.append(i)
		rem.sort()
	
	return (longest,rem) if longest>1 else (0,sorted(arr))



	
