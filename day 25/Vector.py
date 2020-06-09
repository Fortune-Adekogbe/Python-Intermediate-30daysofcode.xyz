class Vector:
    '''
    class for vector type
    '''
    def __init__(self,x,y,z):
        '''
        initializes values in vector
        '''
        assert type(x)==type(z)==type(y)==int
        self.x=x
        self.y=y
        self.z=z
        
    def info(self):
        '''
        returns a sting representing the vector
        '''
        i=str(self.x)+'i'
        j=str(self.y)+'j'
        j="+"+j if self.y>=0 else j
        k=str(self.z)+'k'
        k="+"+k if self.z>=0 else k
        return i+j+k
    
    def magnitude(self):
        '''
        returns the magnitude of the vector
        '''
        a=(((self.x)**2)+((self.y)**2)+((self.z)**2))**0.5
        return round(a,2)

    def __add__(self,B):
        '''
        overloads the addition operator
        '''
        assert type(B)==Vector
        C=Vector(self.x+B.x,self.y+B.y,self.z+B.z)
        return C

    def __sub__(self,B):
        '''
        overloads the subtraction operator
        '''
        assert type(B)==Vector
        C=Vector((self.x-B.x),(self.y-B.y),(self.z-B.z))
        return C

    def __mul__(self,B):
        '''
        overloads the multiplication operator to do dot product of 2 vectors
        or to multply a scalar and a vector
        '''
        assert type(B)==int or type(B)==Vector
        if type(B)==int:
            return Vector(B*self.x,B*self.y,B*self.z)
        else:
            return (self.x*B.x)+(self.y*B.y)+(self.z*B.z)

    def __pow__(self,B):
        '''
        Overloaded power operator to do cross product of 2 vectors
        '''
        assert type(B)==Vector
        #Do cross product
        x=self.y*B.z-self.z*B.y
        y=self.x*B.z-self.z*B.x
        z=self.x*B.y-self.y*B.x
        return Vector(x,-y,z)
    
    def __eq__(self,B):
        '''
        oerloads the equality boolean to check if the magnitude of to vectors are equal
        '''
        assert type(B)==Vector
        return self.magnitude()==B.magnitude()
    
        



