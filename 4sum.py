#highly innefficient (brute force approach) but good exercise in figuring out all possible permutations
#Time complexity: O(n^4)
def fourSum(nums, target): 
    a = 0
    b = 0
    c = 0
    d = 0
    solutions_list = []
    for a in range(len(nums)):
        for b in range(len(nums)):
            for c in range(len(nums)):
                for d in range(len(nums)):
                    x = nums[a]
                    y = nums[b]
                    z = nums[c]
                    w = nums[d]
                    if (x + y + z + w == target) and (a!=b) and (a!=c) and (a!=d) and (b!=c) and (b!=d) and (c!=d):
                        soln = [x, y, z, w]
                        soln.sort()
                        if soln not in solutions_list:
                            solutions_list.append(soln)
    return solutions_list

