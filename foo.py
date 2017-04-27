    
def dataSort(sequence):
    copy=sequence
    n=3
    xResult=[]
    yResult=[]
    currList=[]

    for i in sequence:      #getXlist
        for j in range(n):
            currList.append(copy[j])
            if len(copy) < n: break
        if len(currList)==n:
            xResult.append(currList)
        currList=[]
        copy.pop(0)
        
        
    # for i in sequence:
    #     for j in range(n):
    #         print(n)
    #         currList.append(i)
    #         if len(list(copy)) < n: break
    #         if len(currList)==n:
    #             xResult.append(currList)
    #         currList=[]
    #         print(copy)
    #         copy %= 10**(len(copy)-1)
    
        
    for k in range(n,len(list(sequence))):      #get yList
        yResult.append(sequence[k])
        
        
def testDataSort():
    print("testing dataSort...", end="")
    assert(dataSort([1,2,3,4,5,6,7]) == [[1,2,3],[2,3,4],[3,4,5],[4,5,6],[5,6,7]], [4,5,6,7])
    print("passed!")


testDataSort()