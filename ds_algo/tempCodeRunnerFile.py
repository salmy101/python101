def contains_duplicates(nums) -> bool:
#         newlist = [] #set up a new empty list to store unique elements
#         for num in nums: #loop through each element in the input list
#             if num in newlist: #if that number is already in the newlist, its a duplicate so return True
#                 return True
#             newlist.append(num) #otherwise add to the newlist
#         return False #false if no duplicates were found when loop is done
    
# #Brute Force Method:

# def contains_duplicates(nums) -> bool:
#   for i in range(len(nums)): #outer loop, using range to access a sequence of indices from 0 - (len(nums)-1)
#     for j in range(i + 1, len(nums)): #inner loop, stating at the number next to i, hence starting range at i + 1 an eneding at the last index relected with len(num) - 1
#       if nums[i] == nums[j]: #comparing every pair, the current number num[i] in the outer loop compared to every number after it, if same then we have a duplicate
#         return True 
#   return False