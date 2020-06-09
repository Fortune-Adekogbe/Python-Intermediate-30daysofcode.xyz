def wedding_chow(s):
    '''
    checks the maximum number of guests that can get complete chow
    '''
    assert type(s)==str and all(i in {'r','s','m','f','d'} for i in s)
    food={'r':0,'s':0,'m':0,'f':0,'d':0}
    for i in s:
        food[i]+=1
    num=len(s)
    for i in food:
        num=min(num,food[i])
    ans=''
    for i in food:
        ans+=i*(food[i]-num)
    return num,ans
