class Node:
    '''
    For each node of the Binary Search Tree
    '''
    def __init__(self,value):
        assert type(value)==int
        self.value=value
        self.left=None
        self.right=None


def insert(root,value):
    '''
    inserts a single value into the BST
    '''
    if value<=root.value:
        if not root.left:
            root.left=Node(value)
        else:
            insert(root.left,value)
    else:
        if not root.right:
            root.right=Node(value)
        else:
            insert(root.right,value)

def insert_to_tree(arr):
    '''
    inserts elements of an array into the tree in order
    '''
    assert type(arr)==list
    assert all(type(i)==int for i in arr)
    root=Node(arr[0])
    for i in range(1,len(arr)):
        insert(root,arr[i])
    return root

def max_height(root):
    '''
    Finds maximum height of nodes
    '''
    assert type(root)==Node 
    
    return mh(root)

def mh(root):
    '''
    works in the max_height function
    '''
    if root==None:
        return 0
    else:
        return 1+max(mh(root.left),mh(root.right))



