'''
An array with only one element should yield an empty array for its tail
An empty array should yield an empty array for its tail

tail()
The tail function should be returning a new array and not modify the original 
array that is passed in. Let's write a test case to ensure this:

words = ["Yo Yo", "Lighthouse", "Labs"]
tail(words) #no need to capture the return value since we are not checking it
assert_equal(len(words), 3) #original array should still have 3 elements!


'''
#FUNCTION assert_equal
def assert_equal(actual, expected):
  if actual == expected:
    print(f"✅✅✅ Assertion Passed: {actual} == {expected}")
  else:
    print(f"🛑🛑🛑 Assertion Failed: {actual} != {expected}")

def tail(arr):
    if not arr:  # Check if the list is empty
        return []
    return arr[1:]  # Return everything except the first element using slice

'''
a method without slicing:
def tail(arr):
    if not arr:  # Check if the list is empty
        return []
    
    result = []
    for i in range(1, len(arr)):  # Start loop from index 1
        result.append(arr[i])
    
    return result

'''
