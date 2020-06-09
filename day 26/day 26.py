#merge sort using 2 functions
def Merge(a,b):
    '''
    merges two sorted arrays
    '''
    i=0
    j=0
    ans=[]
    while(i<len(a) and j<len(b)):
        if a[i]<=b[j]:
            ans.append(a[i])
            i+=1
        else:
            ans.append(b[j])
            j+=1
    ans+=a[i:]
    ans+=b[j:]
    return ans

def MergeSort(a):
    '''
    sorts array a
    '''
    n=len(a)
    if n<=1:
        return a
    else:
        ls=MergeSort(a[:int(n/2)])
        rs=MergeSort(a[int(n/2):])
        return Merge(ls,rs)
    

#merge sort using only one function
def MERGE(A):
    if len(A)<=1:
        return A
    else:
        n=len(A)
        a=MERGE(A[:int(n/2)])
        b=MERGE(A[int(n/2):])
        i=0
        j=0
        ans=[]
        while(i<len(a) and j<len(b)):
            if a[i]<=b[j]:
                ans.append(a[i])
                i+=1
            else:
                ans.append(b[j])
                j+=1
        ans+=a[i:]
        ans+=b[j:]
    return ans

#testing
#a=[i for i in range(10,-20,-1)]
#print(a)




def long_pal(s):
    '''
    returns longest palindrome in a string
    '''
    odd=''
    even=''
    longest=None
    #checking for odd palindromes
    for i in range(0,len(s)):
        l,r=i-1,i+1
        pal=s[i]
        while l>=0 and r<=len(s)-1:
            if s[l]==s[r]:
                pal+=s[r]
                pal=s[r]+pal
                l-=1
                r+=1
            else:
                break

        
        if len(pal)>len(odd):
            odd=pal
            
    #checking for even palindromes
    for i in range(0,len(s)-1):
        l,r=i,i+1
        pal=''
        while l>=0 and r<=len(s)-1:
            if s[l]==s[r]:
                pal+=s[r]
                pal=s[r]+pal
                l-=1
                r+=1
            else:
                break
            
        if len(pal)>len(even):
            even=pal

    #returns the longer one
    if len(even)>len(odd):
        return even
    return odd,even
        
#string = "rrccbbccrreef"

#print(long_pal(string))


def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        ans=1
        for i in range(2,n+1):
            ans*=i
        return ans

def C(n,r):
    return factorial(n)/(factorial(n-r)*factorial(r))

def probability(f,d,n,r):
    '''
    gets the probablity of
    n the desired value
    showing up on a number of dice
    when d number of dice with f faces are thrown
    Explanation of this is more of proabability than programming
    '''
    assert type(f)==type(d)==type(n)==int
    assert all(type(i)==int for i in r)
    assert n<=f and r[0]>0 and r[-1]<=f
    p=0
    for i in r:
       a=C(d,i)*(1/(f**i))*((1-(1/f))**(d-i))
       p+=a
    return round(p,4)


p=probability
print(p(6,3,6,range(1,4)))
