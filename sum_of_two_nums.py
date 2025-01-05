#Given two integer numbers, write a Python code to return their product only 
# if the product is equal to or lower than 1000. Otherwise, return their sum.#

# number1 = 20
# number2 = 30
# number1 = 40
# number2 = 30
# product = number1 * number2
# sum = number1 + number2

# if product >= 1000:
#   print('The product is:', product)
# else:
#   print('The sum is:',sum)


# NOW LETS WRITE THIS AS A FUNCTION THAT ACCEPTS TWO NUMBERS FROM THE USER
number1 = int(input("what is your first number: "))
number2 = int(input("what is your second number: "))

def sum_of_two_nums():
  product = number1 * number2
  sum = number1 + number2

  if product <= 1000:
    print('The product is:', product)
  else:
    print('The sum is:',sum)

sum_of_two_nums()