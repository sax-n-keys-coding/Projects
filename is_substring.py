#assuming a string permutation is a substring of a string
def is_substringOrig(str1,str2):
    """
    str1 --> potential substring
    str2 --> orig string
    
    Tests:
    is_substring("a", "at") --> True
    is_substring("ct", "cat") --> True
    is_substring("tc", "cat") --> ????
    Permutations essentially (order matters)
    
    """
    def helper(str1, str2, strBuild):
        if strBuild == str1: # base case order is important, I got this wrong -- 
        #if last character of str2 is kept/not kept (only when kept does this matter), then str2 will be "" when we do str2[1:], 
        #if we test for str2 emptiness, we avoid a lot of cases with the last character of str2
        #therefore, we need to test for equivalency of strBuild (which inherits the last character of str2) with str1 (which can contain the last character of str2) 
        #before we check if str2 is empty (which it is, by this point)
        #this is why I got a lot of cases wrong such as is_substring("ct", "cat") -- because I was lazy to analyze the workings of the problem 
        #i'm still due to make a two var version, which would greatly optimize the space of this function
            return True
        if str2 == "" or str1 == "": ##when parsed through str2, str2 == "".      str1 == "" must be 
        #no need to check further for substrings (no more chars) <-- thus this cond stops recursion -- thus it's a base case
            return False
        else:
            #keep, don't keep -- with/without
            return helper(str1, str2[1:], strBuild + str2[0]) or helper(str1, str2[1:], strBuild) # more intuitive approach, after working out it on a piece of paper 
            #with a with/without binary decision tree
   
    return helper(str1, str2, "")

# now, I couldnt do this with only two variables -- 
#which would optimize the entire process as every frame that the recursive function calls has to store three variables 
#which adds to alot -- ill look at cs61A course notes to see the solution. 

def is_substring(str1, str2): #two vars solution done!! (more elegant and more space-optimized) 
    #it fails for cases like is_substring("ca","cat") --> stringIndexOutOfRange Error Thrown
    if str1 == str2: 
        return True
    elif str1 == "":
        return True
    elif str2 == "":
        return False
    elif str1[0] == str2[0]: #since char is common, 
        #check to see if other chars are common as well
        return is_substring(str1[1:], str2[1:])
    else:
        return is_substring(str1, str2[1:]) 
        #when str1[0] != str2[0] (i.e. 't' in 'ct' != 'a' in 'cat' -- from is_substring('ct', 'cat')
        #we must move on in str2, to match str1, if possible) 
        #(we're iterating through left to right on orig string so a substring is any kept or not-kept character) 

def isSubstringBooklike(str1, str2): # a cleaner version, works as well, but I think above is more efficient 
#works for all cases, even beats the one above
    if str1 == str2: # if str1 a substring of str2, then this will return true
        return True
    elif str2 == "": # when fully iterated through list
        return False
    else:
        return isSubstringBooklike(str1[1:], str2[1:]) or isSubstringBooklike(str1, str2[1:])


#as close as I got to listing all substrings, return is wrong:

def listAllSubstr(string):
        substrLst = []
        stringCopy = string
        stringBuild = ""
        def helper(string, stringBuild):
            if string == "":
                substrLst.append(stringBuild)
                if stringBuild == "":
                    return substrLst                
            else:
                return helper(string[1:], stringBuild + string[0]), helper(string[1:], stringBuild)
        return helper(string, "")

print(listAllSubstr("at"))


