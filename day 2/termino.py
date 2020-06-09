def termino(s):
    '''
    checks how many characters ned o be removed to make all open brackets closed
    '''
    assert type(s)==str and all(i in {'(',')'} for i in s)
    i=0
    no_pairs=0#no of open close bracket pairs
    while i<=len(s)-2:
        if s[i]=='(' and s[i+1]==')':
            no_pairs+=1
            i+=2
        else:
            i+=1
    return len(s)-no_pairs*2
