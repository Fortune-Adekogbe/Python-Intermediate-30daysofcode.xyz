
def rot_line(arr,st,end):
    #rotates a particular loop of an array
    n=len(arr)-1
    for i in range(st,end):
        temp=arr[st][i]
        a,b=st,i
        for i in range(3):
            arr[a][b]=arr[n-b][a]
            a,b=n-b,a
        arr[a][b]=temp

def read_loop(arr,st,m,n):
    '''
    Reads one cyclic path of a 2d array
    m is the row index of right bottom corner
    n is the column index of the right bottom corner
    st is the index of the top left corner
    '''
    ans=''
    if st==m:
        for i in range(st,n+1):
            ans+=str(arr[st][i])+' '
        return ans
    elif st==n:
        for i in range(st,m+1):
            ans+=str(arr[i][st])+' '
        return ans
    #moving right on first row forward
    for i in range(st,n):
        ans+=str(arr[st][i])+' '
    #moving down on right side
    for j in range(st,m):
        ans+=str(arr[j][n])+' '

    #mooving to the left on last row
    for k in range(n,st,-1):
        ans+=str(arr[m][k])+' '
        
    #moving up on the left side
    for l in range(m,st,-1):
        ans+=str(arr[l][st])+' '
    
    return ans











#THE MAIN FUNCTIONS THAT WE ARE USING
def loop_read(arr):
    '''
    reads from a 2D array cyclicly
    '''
    assert all(type(i)==list for i in arr)
    assert all(all(type(i)==int for i in j) for j in arr) or  all(all(type(i)==str for i in j) for j in arr)
    start=0
    m=len(arr)-1
    n=len(arr[0])-1
    ans=''
    while start<=m and start<=n:
        ans+=read_loop(arr,start,m,n)
        start+=1
        m-=1
        n-=1
    return ans[:-1]

def rotate(arr):
    '''
    rotates an array by 90 degrees
    '''
    assert all(type(i)==list and len(i)==len(arr) for i in arr )
    assert all(all(type(i)==int for i in j) for j in arr)
    start=0
    end=len(arr)-1
    while start<=end:
        rot_line(arr,start,end)
        start+=1
        end-=1

'''

        
def printMat(arr):
    for i in arr:
        print(i)

for i in range(97,97+5):
    eval('printMat(eval(chr(i)))')
    print()
    eval('rotate(eval(chr(i)))')
    eval('printMat(eval(chr(i)))')
    print()


printMat(e)
print()
rotate(e)
printMat(e)
'''


