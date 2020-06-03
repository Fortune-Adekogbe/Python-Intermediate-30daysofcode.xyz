
def isSum(arr,num,n):
    '''
    checks if sum can be gotten from array.
    its recursion using memoization
    this could also be solved by using dynamic programming
    '''
    data=[[None for i in range(n+1)] for j in range(num+1)]
    return IS(arr,num,n,data)
    

def IS(arr,num,n,data):
    '''
    works hand i hand with the function above it
    '''
    if num==0:
        data[num][n]=True
        return True
    if n<1:
        return False
    else:
        if data[num][n]!=None:#if it has already been calculated before
            return data[num][n]
        else:#calculate it and add it to the storage array
            data[num][n]=IS(arr,num-arr[n-1],n-1,data) or IS(arr,num,n-1,data)
            return data[num][n]


def my_money(arr):
    '''
    to check if money can be shared equally
    '''
    assert all(type(i)==int and i>0 for i in arr)
    if len(arr)==1:
        return False
    s=sum(arr)
    if s&1:
        return False
    else:
        return isSum(arr,int(s/2),len(arr))
    

                   


                    
#using recursion
def combo(arr,n):
    '''
    all oomdinations of n elements from the array
    '''
    assert all(type(i)==int for i in arr)
    assert n>0
    if n==1:
        #if n =1 then return all individual elements of the array
        ans=[[i] for i in arr]
        return ans
    elif n==len(arr):
        #if n = the length of the array
        #return the whole array
        return [arr]
    else:
        ans=[]
        for i in range(len(arr)-n+1):
            ans=ans+[[arr[i]]+ j for j in combo(arr[i+1:],n-1)]
        return ans


