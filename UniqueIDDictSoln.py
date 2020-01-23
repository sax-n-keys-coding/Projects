"""
PROBLEM OVERVIEW:

Each breakfast delivery is assigned a unique ID, a positive integer. 
When one of the company's 100 drones takes off with a delivery, 
the delivery's ID is added to an array, deliveryIdConfirmations. 
When the drone comes back and lands, the ID is again added to the same array.

After breakfast this morning there were only 99 drones on the tarmac. One of the drones never made it back from a delivery. 
We suspect a secret agent from Amazon placed an order and stole one of our patented drones. 
To track them down, we need to find their delivery ID.

Given the array of IDs, which contains many duplicate integers and one unique integer, find the unique integer.

Problem source: https://www.interviewcake.com/question/java/find-unique-int-among-duplicates
"""

def uniqueID(lst): #time complexity (I think): O(n)
    dictIds = {}
    for idNum in lst:
        if idNum in dictIds:
            dictIds[idNum] += 1
        else:
            dictIds.update({idNum:1})
    for idNum in dictIds.keys():
        tmp = dictIds[idNum]
        if tmp % 2 == 1:
            return idNum
    return "There is no unique key in list"
    
uniqueID([1123123,92391230,12391239, 92391230,1123123,12391239, 12391239, 1234567,1234567,12391239, 12391239]) 

#Correction #1:
#missing drone could have instances that are greater than 1, in fact:
#the number of indices for the missing drone (uniqueID) will always be odd 

#(a drone could take off and land some times and then get lost, thus making the drone ID's occurences odd)
