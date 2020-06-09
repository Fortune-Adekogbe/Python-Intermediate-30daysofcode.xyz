
def bubble_sort(arr):
    '''
    Arranges all the elements of an array in ascending order using
    bubble sort algorithm
    '''
    assert type(arr)==list
    assert all(type(i)==int for i in arr)
    n=len(arr)-1
    swaps=0
    for i in range(n):
        for j in range(n-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swaps+=1
    return swaps





