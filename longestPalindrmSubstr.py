strList = []
def substrLister(string, stringBuild): #think that this is redundant, because of many “” 
    #results, but I may be wrong
    #I believe this works
        if string == "":
            strList.append(stringBuild)
            return None
        return substrLister(string[1:], stringBuild + string[0]), substrLister(string[1:], stringBuild)

substrLister("at", "")



def longestPalindrmSubstr(string):
    strList = []
    def substrLister(string, stringBuild): #think that this is redundant, because of many “” 
    #results, but I may be wrong
    #I believe this works
        if string == "":
            strList.append(stringBuild)
            return None
        return substrLister(string[1:], stringBuild + string[0]), substrLister(string[1:], stringBuild)
    
    
    def isPalindrm(string): 
    # easy way to just do string[-1] == string 
    #string[::-1] reverses any iterable, such as this string (a palindrome fits this definition #perfectly -- a palindrome is a string that is the same read from the front as read from #the back (i.e. “eye”)
    #but I want to code recursively by hand
        lengthStr = len(string) - 2
        def helper(string, length):
            if string[0] == string[-1]:
                    return helper(string[1:lengthStr], lengthStr - 1) # some counting issue, with some bugs, but I hope this is ok
            elif string == "":
                    return True
            else: 
            #not equal and not empty, then automatically its not a palindrome, so its
            #false
                    return False
        return helper(string, lengthStr)
        
    #main
    substrLister(string[1:], "")
    plndrmStrList = []
    for indSubstr in range(len(strList)):
        tmp = strList[indSubstr]
        if isPalindrm(tmp):
            plndrmStrList.append(tmp)
    
    #map(len(), plndrmStrList) <-- I believe that's the usage
    
    for subStr in plndrmStrList:
        subStr = len(subStr)
    
    return max(plndrmStrList)
    
    longestPalindrmSubstr("at")