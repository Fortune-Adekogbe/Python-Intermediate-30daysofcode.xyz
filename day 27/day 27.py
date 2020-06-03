'''
code for day 27 in 30 days of code may edition
'''

def isBalanced(s,index=0,check=[]):
    '''
    checks if a string of parentheses is balanced
    * could represent a prentheses or an empty string
    '''
    assert type(s)==str
    assert all( i in {'(',')','*'} for i in s)
    if all(i =='*' for i in s):
        return True
    if index==len(s):
        if len(check)==0:
            return True
        else:
            return False
        
    if s[index]==')' and len(check)==0:
        return False
    else:
        if s[index]=='(':
            check.append(s[index])
            return isBalanced(s,index+1,check)
        elif s[index]==')':
            check.pop(-1)
            return isBalanced(s,index+1,check)
        else:
            n_check=[i for i in check]
            a=isBalanced(s,index+1,check+['('])#taking the * as an opening parentheses
            b=isBalanced(s,index+1,check)#taking the * as an empty string
            if len(n_check)>0:
                n_check.pop(-1)
                c=isBalanced(s,index+1,n_check)#taking it as a closing parentheses
                return a or b or c
            return a or b

def isPalindrome(s):
    '''
    checks if a string is a palindrome
    '''
    i=0
    j=len(s)-1
    while i<j:
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True

def match(los):
    '''
    checks for two strings that concatenate to form a palindrome
    '''
    assert type(los)==list
    assert all(type(i)==str for i in los)
    ans=[]
    for i in range(len(los)):
        for j in range(len(los)):
            if i!=j and isPalindrome(los[i]+los[j]):
                ans.append((i,j))
    return ans

