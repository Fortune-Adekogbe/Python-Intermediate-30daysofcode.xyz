
def binary(n,n_bits):
    '''
    converts integer n to a binary number of n bits
    '''
    ans=''
    while n>0:
        ans=str(n&1)+ans
        n=n>>1
    while len(ans)<n_bits:
        ans='0'+ans
    return ans

def bits_of_gray(n_bits):
    '''
    returns the gray code order of n_bits
    '''
    assert type(n_bits)==int and n_bits>0
    ans=[]
    for i in range(2**n_bits):
        a=i^(i>>1)
        ans.append(binary(a,n_bits))
    return ans

