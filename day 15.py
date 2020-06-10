class Fraction(object):
    def __init__(self,val):
        assert type(val)==str,f'{val} is a wrong input'
        assert val.replace('/','',1).isnumeric(),f'{val} is a wrong input'
        self.numer  = int(val.split('/')[0])
        self.denom =  int(val.split('/')[1])


def lcm(l):
    '''
    A function to compute LCM
    :param l: a list of integers
    :type l: list
    :return: the lowest common multiple
    :rtype: float
    '''
    h = 1
    for i in range(2,min(l)):
        while all(map(lambda i: i%1==0,l)):
            l = [j / i for j in l]
            h*=i
        h/=i
        l = [j*i for j in l]
    for i in l:
        h*=i
    print(h)
    return h if h%1==0 else h//1+1


def adder(arr):
    """
    A function that sums fractions.
    :param arr: an array of fractions represented as strings
    :type arr: list
    :return: fraction representing the sum of the fractions in arr
    :rtype: string
    """
    assert type(arr)==list,f'{arr} is an invalid input'
    classed = [Fraction(i) for i in arr]
    denominators = [j.denom for j in classed]
    biggie=1
    for i in denominators:
        biggie *= i
    summing = int(sum([biggie*i.numer/i.denom for i in classed]))
    x = gcd(summing,biggie)
    while x!=1:
        summing,biggie = summing/x,biggie/x
        x = gcd(summing, biggie)
    return f'{int(summing)}/{int(biggie)}'


#print(adder(['95/2','8/90',0.33]))

def swap(a, b):
    '''
    Swaps integers a and b
    :param a: varible 1
    :type a: int
    :param b: variable 2
    :type b: int
    :return: the swapped variables
    :rtype: tuple
    '''
    assert type(a) == type(b) == int, 'Invalid input'
    a ^= b
    b ^= a
    a ^= b
    return a,b
e = '''print(swap(2.0,8.0))
import inspect
print(inspect.getsource(swap).count('^')==3)'''

def errorr(l):
    try:
        x=adder(l)
    except AssertionError:
        return True
    except:
        return False
    else:
        return x
exec(e)
print(errorr(['95//2','8/90','2/6']))
