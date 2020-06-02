def itos(i):
    '''
    converts integer to string
    '''
    if type(i)!=int:
        raise ValueError
    s=''
    isNeg=i<0
    i=abs(i)
    while(i>0):
       d=i%10
       i//=10
       s=chr(ord('0')+d)+s
    return s if not isNeg else '-'+s

def stoi(s):
    '''
    converts string to integer
    '''
    try:
        s+''
    except:
        raise ValueError
    if '.' in s:
        raise ValueError
    
    isNeg = (s[0] == '-')
    s = s[1:] if isNeg else s
    ans=0
    for i in s:
        ans=ans*10+ord(i)-ord('0')
    return ans if not isNeg else ans*-1

def stof(s):
    '''
    converts string to float
    '''
    try:
        s+''
        s.index('.')
    except:
        raise ValueError
    isNeg=s[0]=='-'
    s=s[1:] if isNeg else s
    ind=s.index('.')
    whole=0
    frac=0
    for i in range(ind):
        whole=whole*10+ord(s[i])-ord('0')
    for i in range(len(s)-1,ind,-1):
        frac=(frac/10)+(ord(s[i])-ord('0'))
    f_ans=whole+frac/10 
    return  f_ans*(-1) if isNeg else f_ans  

        
def ftos(f):
    '''
    converts float to string. Not 100% accurate though
    '''
    if type(f)!=float:
        raise ValueError
    isNeg=f<0
    f=abs(f)
    w=round(f)
    if w>f:
        w-=1
    ans=itos(w)
    r=f-w
    a='.'
    while(r>0):
        r*=10
        d=round(r)
        if d>r:
            d-=1
        a+=chr(ord('0')+d)
        r-=d
    return ans+a if not isNeg else ('-'+ans+a)


