# import maskpass

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

# password checker

username = input("please type the username")
password = input("please type the password")
# password = maskpass.askpass( prompt="please type the password", mask="*") */
password_length = len(password)
hideden_password = "*" * password_length
print(f"{username}, your password {hideden_password} is {password_length} long")

# Lists

amazon_cart = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(amazon_cart[0:3])
amazon_cart[0]= 0
print(amazon_cart)

# Maxtrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0][2])
print(matrix[1][1])

# List methods

basket = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(len(basket))

# adding
basket.append(11)
new_basket = basket.append(12)
# new_basket is None because append method returns None, same goes for insert and extend methods
print(new_basket)
print(basket)
basket.insert(0, 0)
print(basket)
basket.extend([12, 13, 14])
print(basket)

# removing

basket.pop()
# pop method returns the removed item
new_basket = basket.pop()
print(new_basket)
print(basket)
basket.pop(0)
print(basket)
basket.remove(12)
print(basket)
basket.clear()
print(basket)

bucket  = ['a', 'b', 'c','x', 'd', 'e', 'd']
print(bucket.index('d'))
#search for d from index 0 to 5
print(bucket.index('d', 0, 5))
print(bucket.count('d'))

# sorting

bucket.sort()
print(bucket)
bucket.reverse()
print(bucket)

