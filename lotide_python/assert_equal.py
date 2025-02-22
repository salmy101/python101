'''
If the values match, it should print (console.log) the following: Assertion Passed: [actual] === [expected] (but with the values filled in)
Otherwise it should print (console.log) the following: Assertion Failed: [actual] !== [expected] (but with the values filled in)

Test at least the following scenarios:

Comparing identical strings
Comparing non-identical strings
Comparing identical numbers
Comparing non-identical numbers

'''

#FUNCTION IMPLEMENTATION
def assert_equal(actual, expected):
  if actual == expected:
    print(f"✅✅✅ Assertion Passed: {actual} == {expected}")
  else:
    print(f"🛑🛑🛑 Assertion Failed: {actual} != {expected}")

#TEST CODE
assert_equal("Lighthouse Labs", "Lighthouse Labs")
assert_equal("Lighthouse Labs", "Bootcamp")
assert_equal(1, 1)
assert_equal(1,51)