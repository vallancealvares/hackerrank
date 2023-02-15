#!/usr/bin/env python

#
# Complete the 'fizzbuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
  # Write your code here
  for i in range ( i, n + 1):
    if (i%3==0 and i%5==0):
      print('FizzBuzz')
    elif (i%3==0):
      print('Fizz')
    elif (i%5==0):
      print('Buzz')
    else :
      print(i)
      
if __name__ == '__main__'
