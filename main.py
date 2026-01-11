#Functons
from functools import reduce


def say_hello():
  print('hellloooo')


say_hello()

#parameters and  arguments


#parameters are the variables that are defined in the function definition
def say_hello(name, emoji):
  print(f'hellloooo {name} {emoji}')


#arguments are the values that are passed to the function when it is called
say_hello('John', ':)')

# function modifies something in a prograam or return something


# return
def sum(num1, num2):
  return num1 + num2


print(sum(4, 5))

#Exercisea
age = input("What is your age?: ")

if int(age) < 18:
  print("Sorry, you are too young to drive this car. Powering off")
elif int(age) > 18:
  print("Powering On. Enjoy the ride!")
elif int(age) == 18:
  print("Congratulations on your first year of driving. Enjoy the ride!")

# convert aboove code to a function


def checkDriverAge(age):

  if int(age) < 18:
    print("Sorry, you are too young to drive this car. Powering off")
  elif int(age) > 18:
    print("Powering On. Enjoy the ride!")
  elif int(age) == 18:
    print("Congratulations on your first year of driving. Enjoy the ride!")


checkDriverAge(18)

# *args and **kwargs

# *args and **kwargs are used to pass a variable number of arguments to a function

def  super_func(*args, **kwargs):
  print(args)
  print(kwargs)
  totol = 0
  for item in args:
    totol += item
  return totol
   # kwargs is a dictionary of keyword arguments

print(super_func(1,2,3,4,5, num1=5, num2=10))

#exercise , highest even number in a list

def highest_even(li):
   evens = []
   for item in li:
     if item % 2 == 0:
       evens.append(item)
   return max(evens)

print(highest_even([10,2,3,4,8,11]))

# mape , filter, zip and reduce
# map, filter, zip and reduce are built-in functions that are used to apply a function to a sequence of elements and return a list of the results

def  multiply_by2(item):
  return item * 2

print(list(map(multiply_by2, [1,2,3])))

def  check_even(item):
  return item % 2 == 0
   # filter will return a list of items that are true for the function
print(list(filter(check_even, [1,2,3])))

# zip will return a list of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables
print(list(zip([1,2,3], [4,5,6])))

# example we  have 2 lists of names and ages and we want to combine them into a list of tuples
# reudce will apply a function of two arguments cumulatively to the items of a sequence, from left to right, so as to reduce the sequence to a single value

def  accumulator(acc, item):
   return acc + item

print(reduce(accumulator, [1,2,3], 1))