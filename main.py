print("Hello, World!")
name = input("what is your name?")
print("helooooo " + name)


# Guess the output of each answer before you click RUN
# Try to write down your answer before and see how you do... keep it mind I made it a little tricky for you :)

print((5 + 4) * 10 / 2)

print(((5 + 4) * 10) / 2)

print((5 + 4) * (10 / 2))

print(5 + (4 * 10) / 2) # 25

print(5 + 4 * 10 // 2) # 25

age = 33

print(f'Hi {name}, you are {age} years old')


# 1 What would be the output of the below 4 print statements? 
#Try to answer these before you click RUN!

print("Hello {}, your balance is {}.".format("Cindy", 50))

print("Hello {0}, your balance is {1}.".format("Cindy", 50))

print("Hello {name}, your balance is {amount}.".format(name="Cindy", amount=50))

print("Hello {0}, your balance is {amount}.".format("Cindy", amount=50))



# string indexing

selfish = "01234567"

# start:stop:stepover
print(selfish[0:2])
print(selfish[0:8:2])
print(selfish[0:8:3])
print(selfish[1:])
print(selfish[:5])
print(selfish[::1])
# in python negative index means start from the end
print(selfish[-1])
print(selfish[-4])
# reverse the string quick trick
print(selfish[::-1])

# string is immutable , you can't change it

# selfish[0] = '8' # this will throw an error
selfish = "hello"
print(selfish)


# built in functions + methods

action  = "i am learning  python"
print(action.upper())
print(action.capitalize())

print(action.find('python'))
print(action.replace('python', 'Golang'))

print(action)
 # string is immutable , so action  will not change

action2 = action.replace('python', 'Golang')
print(action2)

## Type conversion
## exercise 

birth_year = input("which year you were born?")
my_age = 2025 - int(birth_year)
print(f"your age is {my_age}")