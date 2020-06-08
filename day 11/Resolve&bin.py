def resolve(dic,e_list):
    '''
    resolves all elements in e_list using dic
    '''
    assert type(dic)==dict
    assert all([(type(i)==str and i.isalpha()) or (type(i)==int and i>0) for i in dic])
    assert all([(type(dic[i])==str and dic[i].isalpha()) or type(dic[i])==int for i in dic])
    assert all([(type(i)==str and i.isalpha()) or type(i)==int for i in e_list])
    ans=[]
    for i in e_list:
        ans.append(f_map(dic,i))
    return ans

def f_map(dic,ele):
    '''
    resolves an element e
    '''
    if ele not in dic:
        return ele
    else:
        s=set()
        while ele in dic:
            if ele not in s:
                s.add(ele)
                ele=dic[ele]
            else:
                return ele
        return ele

def bin(lis,llim):
    '''
    docstring
    '''
    assert all(type(i)==int for i in lis)
    assert all(type(i)==int for i in llim)
    ans=[0]*len(llim)
    lis.sort()
    j=0
    #llim[j] is the lower limit in each iteration
    for i in range(len(lis)):
        if j+1<len(ans):
            if lis[i]>=llim[j+1]:
                j+=1
                ans[j]+=1
            elif lis[i]>=llim[j]:
                ans[j]+=1
        else:
            ans[j]+=len(lis)-i
            break

    return ans if len(llim)>0 else [0]
        
        
    
