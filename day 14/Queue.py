class Node:
    '''
    class for each node of the queue
    '''
    def __init__(self,value):
        assert type(value)==int
        self.value=value
        self.next=None


class Queue:
    '''
    class for a queue
    FIFO data structure
    '''
    def __init__(self):
        self.head=None

    def front(self):
        '''
        returns the first element in the queue
        if queue is empty the return None
        '''
        if self.head==None:
            return None
        return self.head.value


    def count(self):
        '''
        count the number of elements in the queue
        '''
        c=0
        head=self.head
        while head:
            head=head.next
            c+=1
        return c
        

    def enqueue(self,value):
        '''
        adds an element to the back of the queue
        '''
        assert type(value)==int
        if self.head==None:
            self.head=Node(value)
        else:
            h=self.head
            while h.next:
                h=h.next
            h.next=Node(value)
            

    def dequeue(self):
        '''
        removes an element from the front of the queue and
        returns the value of that element
        '''

        if self.head==None:
            raise AssertionError
        else:
            a=self.head.value
            self.head=self.head.next
            return a
        

        
