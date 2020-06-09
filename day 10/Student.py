class Student:
    def __init__(self,age,weight,height):
        assert type(age)==int
        assert type(weight)==float
        assert type(height)==float
        self.age=age
        self.weight=weight
        self.height=height
        
    def info(self):
        bmi=round(self.weight/(self.height**2),2)
        return (self.age,bmi)

def average(lis):
    '''
    dostring
    '''
    assert type(lis)==list
    assert all([type(i)==Student for i in lis])
    a,w,h=0,0,0
    for i in lis:
        a+=i.age
        w+=i.weight
        h+=i.height

    w*=(1.05**10)
    h*=(1.02**10)
    n=len(lis)
    return (round(a/n+10,2),round(w/n,2),round(h/n,2))

