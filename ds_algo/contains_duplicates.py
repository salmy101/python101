'''
Problem Statement
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums= [1, 2, 3, 4]
Output: false  
Explanation: There are no duplicates in the given array.

'''

#My original Method:

# def contains_duplicates(nums) -> bool:
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

#Hash Set Method:

def contains_duplicates(nums) -> bool:
  unique_set = set() #a set is a data structure that only holds unique elements
  for x in nums: #no need to use indices, lets just look at the num
    if x in unique_set: #if the number is already in the unique_set, than we have a duplicate! return True and done
      return True #otherwise add the number to the set and keep looping
    unique_set.add(x)
  return False #if you never find a duplicate return False

# print(contains_duplicates([1,2,3,1])) #output is True
# print(contains_duplicates([1,2,3,4])) #output is False
# print(contains_duplicates([1,1,1,3,3,4,3,2,4,2])) #output is True

'''
Key Idea
1) A set in Python is a data structure that only stores unique elements. This means:

If you try to add a duplicate element to a set, it will simply ignore the addition.
Checking if an element exists in a set is very fast (average time complexity of O(1)).
By leveraging these properties, we can efficiently detect duplicates in a list.

2)for x in nums of hash set methof:

Instead of using indices (for i in range(len(nums))), this loop directly iterates over the elements of the list. This makes the code cleaner and easier to read.

3) Comparison with Brute Force and my method
Aspect	          Brute Force	                  Hash Set Method                 My original method
Time Complexity	  O(n^2)	                      O(n)                            O(n^2) =  The 'if num in newlist' check involves searching through the list, which takes O(n) in the worst case (if the element is not in the list or is at the end).Since this check happens for each element in the loop, the overall time complexity is O(n^2).
Space Complexity	O(1)	                        O(n)                            O(n)
Code Readability	More complex (nested loops)	  Simpler (no indices)
Efficiency	      Poor for large inputs	        Excellent for large inputs


4) My originla method
solution works, it is less efficient than the hash set method because of the O(n^2) search time for each element in the list. 
The hash set method avoids this by leveraging the fast lookup property of sets. A hash set Time Complexity: O(n) 
(because checking if an element exists in a set is O(1) on average).


'''

my_set = set()

my_set.add(1)
my_set.add(2)
my_set.add(2)
my_set.add(3)
print(my_set)

'''practicing with sets, adding an elementthat is already in a set is completely ignored, cool. 
also making not of my use of .append() will add to the end of a list and allows for a duplicate
 .add() will add unique element to set

'''