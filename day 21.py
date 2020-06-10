def overflow(image,start,filler,pivot,debug = True):
    """
    This flood fills an image with a variable.
    :param image: A matrix representing the image
    :type image: list
    :param start: the coordinates of the start point
    :type start: tuple
    :param filler: The integer to be filled into the image
    :type filler: int
    :param pivot: This represents the pivot element
    :type pivot: int
    :param debug: This helps identify the first iteration of the recursion
    :type debug: bool
    :return: The flood filled image
    :rtype: list
    """
    assert type(start[0]) == type(start[1])== type(filler)==type(pivot)==int
    x,y = start   
    if debug==True :
        assert image[x][y] == pivot
        debug=False
    r = len(image)
    assert all(map(lambda i:type(i)==list,image))
    c = len(image[0])
    if x-1>=0:
        if image[x-1][y]==pivot and image[x-1][y] != filler:
            assert type(image[x-1][y])==int
            image[x-1][y] = filler
            overflow(image,(x-1,y),filler,pivot,debug)
    if x+1<r:
        if image[x+1][y]==pivot and image[x+1][y] != filler:
            assert type(image[x+1][y])==int
            image[x+1][y] = filler
            overflow(image,(x+1,y),filler,pivot,debug)
    if y-1>=0:
        if image[x][y-1]==pivot and image[x][y-1] != filler:
            assert type(image[x][y-1])==int
            image[x][y-1] = filler
            overflow(image,(x,y-1),filler,pivot,debug)
    if y+1<c:
        if image[x][y+1]==pivot and image[x][y+1] != filler:
            assert type(image[x][y+1])==int
            image[x][y+1] = filler
            overflow(image,(x,y+1),filler,pivot,debug)
    return image
    