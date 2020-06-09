def checkdict(a_dic):
        '''
        to assert all values in the dictionary are strings
        '''
        assert type(a_dic)==dict
        assert all([type(i)==str and len(i)==1 and i.isupper() for i in a_dic] )
	
def sparsify(a_mat):
	'''
	creates an adjacency matrix
	from a dictionary representing
	a graph
	'''
	checkdict(a_mat)
	for i in a_mat:
		checkdict(a_mat[i])
	n=len(a_mat)
	a=[[0]*n for i in range(n)]#creates a matrix of zeros
	for i in a_mat:
		for j in a_mat[i]:
			c=ord(i)-65
			r=ord(j)-65
			assert type(a_mat[i][j])==int
			a[r][c]=a_mat[i][j]
	return a
#testing
#a={"A":{"B": 2,"D":4}, "B": {"C": 1}, "C": {"A": 3, "D": 1}, "D": {"B": 1}}
#sparsify(a)
#returns [[0, 0, 3, 0], [2, 0, 0, 1], [0, 1, 0, 0], [4, 0, 1, 0]]
