# almost complete, not fast enough
def getLargestNumber(num):

    i = 0
    numCopy = list(num)
    # print(num[i])
    while (i < len(num)-1):
        if(numCopy[i+1] and (int(numCopy[i]) >= int(numCopy[i+1]))):
            i+=1
        elif(numCopy[i+1] and (int(numCopy[i])%2) == (int(numCopy[i+1])%2)):
            numCopy[i], numCopy[i+1] = numCopy[i+1], numCopy[i]
            i = 0
        else:
            i+=1
    res = ''.join(str(n) for n in numCopy)
    return res
