def polyEval(poly, x):
    #polyEval([1, 2, 5])
    f = 0
    for i in range(len(poly)):
        f += (poly[i])*((x)**i)
    return f



def polySum(poly1, poly2):
    listSum = []
    n = 0
    if len(poly1) > len(poly2):
        n = len(poly2)
    else:
        n = len(poly1)

    for i in range(n):
        sum = poly1[i] + poly2[i]
        listSum.append(sum)
    '''
    polySum(
        [1, 2, 5],
        [2, 0, 1, -7
    )
    '''
    if len(poly1) > len(poly2):
        listSum += poly1[n:]
    else:
        listSum += poly2[n:]
    while listSum[-1] == 0:
        listSum.pop(-1)
    return  listSum



def polyMultiply(poly1, poly2):
    result= [0]* (1+len(poly1)-1+len(poly2)-1)
    for i in range(len(poly1)):
        for j in range(len(poly2)):
            result[i+j] += poly1[i]*poly2[j]
    while result[-1] == 0:
        result.pop(-1)
    return result
