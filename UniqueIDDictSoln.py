def uniqueNum(lst):
    dictIds = {}
    for idNum in lst:
        if idNum in dictIds:
            dictIds[idNum] += 1
        else:
            dictIds.update({idNum:1})
    for idNum in dictIds.keys():
        tmp = dictIds[idNum]
        if tmp == 1:
            return idNum
    return "There is no unique key in list"
    
uniqueNum([1123123,92391230,92391230,1123123,12391239,1234567,1234567])