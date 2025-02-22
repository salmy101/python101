''' 
Create a function head which returns the first item in the array.

The head function should not return the first element as an array. It should simply return the element itself.


It would be nice to make use of our handy assertEqual function. Copy it from its source file and paste it into the top of head.js. 
In the future we will learn a better approach to sharing functions between different files, but until then this copy/paste approach will do.

You should always be thinking about other scenarios to consider. Here are some such examples and how they should be handled:
An array with only one element should still yield that one element as its head
An empty array should yield undefined as its head
'''
#FUNCTION assert_equal
def assert_equal(actual, expected):
  if actual == expected:
    print(f"✅✅✅ Assertion Passed: {actual} == {expected}")
  else:
    print(f"🛑🛑🛑 Assertion Failed: {actual} != {expected}")


def head(arr):
  if not arr:
    return None
  return arr[0]

  


assert_equal(head([5, 6, 7]), 5)
assert_equal(head([6]), 6)
assert_equal(head([]), 6)


#this test is using the head function to retun the forst element arr[0], and then verifying it with assert_equalfunction