def minimum(l):
	x=float("inf")
	for i in l:
		if i<x:
			x=i
	return x

def selection(l):
	for i in range(len(l),0,-1):
		a= minimum(l[:i])
		l.remove(a)
		l.append(a)
	return l
	
print(selection([8,7,6,5,4,3,2,6,6,4,4,85,2000,1005]))


def combiner(l,n):
	col = [selection([l[a]]+l[i+a+1:i+a+n]) for i in range(len(l)+1) for a in range(len(l)) if len(selection([l[a]]+l[i+a+1:i+a+n]))==n]
	l=l[::-1]
	lect = [selection([l[a]]+l[i+a+1:i+a+n]) for i in range(len(l)+1) for a in range(len(l)) if len(selection([l[a]]+l[i+a+1:i+a+n]))==n and selection([l[a]]+l[i+a+1:i+a+n]) not in col]

	return col+lect

def short_sub(n,d):
	"""
	A function that returns the shortest sub-string containing the characters in a given set.
	:param n: A string
	:type n: str
	:param d: A set of characters
	:type d: set
	:return: Shortest sub-string
	:rtype: str
	"""
	a = {w:[] for w in d}
	s=[]
	filt = lambda x: len(set(n[i] for i in x)) == len(d)
	for i,j in enumerate(n):
		if j in d:
			a[j].append(i)
			s.append(i)
	v = {d[-1]-d[0]:d for d in filter(filt,combiner(s,len(d)))}
	q = v[min(v.keys())]
	return n[q[0]:q[-1]+1]

print(short_sub('wednesday',{'e','d'}))