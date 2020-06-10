def my_exes(matrix,thresh=None):
	"""
	Count the number of Xs in the given matrix where X are traced by 1s.
	:param matrix: A matrice of 0s and 1s.
	:type matrix: list
	:param thresh: The maximum threshold to be considered.
	:type thresh: int
	:return: The number of Xs within the limit of the threshold
	:rtype: int
	"""
	if thresh != None: assert thresh>0 and type(thresh)==int
	assert all(map(lambda i: type(i)==list and len(i)>1,matrix)) and type(matrix)==list
	assert all(all(map(lambda i: isinstance(i,int) and i in [0,1],j)) for j in matrix)
	count=0
	m=len(matrix)
	n=len(matrix[0])
	l=len(matrix)-1 if thresh is None else thresh
	x = lambda i,j,sq: [sub[j:j+sq] for sub in matrix[i:i+sq]]
	y = lambda matrix,sq: all([matrix[i][i]+matrix[sq-(i+1)][i]==2 for i in range(sq)])
	for sq in range(2,l+2):
		for i in range(m):
			for j in range(n):
				if i+sq<=m and j+sq<=n:
					
					if y(x(i,j,sq),sq):
						print(x(i,j,sq))
						count+=1
	return count
