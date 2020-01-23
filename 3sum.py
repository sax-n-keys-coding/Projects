def threeSum(nums, target): #returns a list of lists with three unique (unrepeated) values that sum to the "target" taken from an input list "nums"
	solutionList = []
	len_nums = len(nums)
	for a in range(len_nums):
	    for b in range(len_nums):
	        for c in range(len_nums):
	            x = nums[a]
	            y = nums[b]
	            z = nums[c]
	            if (x + y + z == target) and (a != b) and (b != c) and (a != c):
	                soln = [x, y, z] 
	                soln.sort()
	                if soln not in solutionList:
	                    solutionList.append(soln)
	return solutionList

