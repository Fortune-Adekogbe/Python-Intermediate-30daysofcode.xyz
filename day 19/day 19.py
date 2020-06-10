def insertion(l):
    """
    An algorithm to implement the insertion sort algorithm
    :param l: An array
    :type l: list
    :return: A sorted array
    :rtype: list
    """
    assert type(l)==list
    for i,j in enumerate(l):
        for m,n in enumerate(l):
            if j<n:
                l.remove(j)
                l.insert(m,j)
                break
            if m==i:
                break
    return l
print(insertion(['a','c','A','e','g','K']))
def biggie(l,n):
    """
    A function that returns the closest larger digit to the digit at the index n in the list l.
    :param l: The list to be considered
    :type l: list
    :param n: The index to be considered
    :type n: int
    :return: The closest largest digit
    :rtype: int
    """
    assert type(l)==list and type(n)==int,"Wrong input type"
    assert 0<n<len(l),f"{n} is out of range"
    mapper = {b:a for a,b in enumerate(l)}
    r,nr=-1,len(l)
    for i in l[:n][::-1]:
        if l[n]<i:
            r=mapper[i]
            break
    for j in l[n+1:]:
        if l[n]<j:
            nr= mapper[j]
            break
    assert r!=-1 or nr!=len(l)
    return nr if (n-r)>=(nr-n) else r
print(biggie([17,5,3,10,3,16],5))