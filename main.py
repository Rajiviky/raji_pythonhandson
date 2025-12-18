#Functons

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

#Exercise

age = input("What is your age?: ")

if int(age) < 18:
  print("Sorry, you are too young to drive this car. Powering off")
elif int(age) > 18:
  print("Powering On. Enjoy the ride!");
elif int(age) == 18:
  print("Congratulations on your first year of driving. Enjoy the ride!")

# convert aboove code to a function

def checkDriverAge(age):

  if int(age) < 18:
    print("Sorry, you are too young to drive this car. Powering off")
  elif int(age) > 18:
    print("Powering On. Enjoy the ride!");
  elif int(age) == 18:
    print("Congratulations on your first year of driving. Enjoy the ride!")

checkDriverAge(18)