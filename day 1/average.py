def average(s):
    '''
    Takes in a string of intergers and sums them up
    '''
    assert type(s)==str
    s=s.split()
    summ=0
    try:
        for i in s:
            summ+=int(i)
    except:
        raise AssertionError

    return summ
