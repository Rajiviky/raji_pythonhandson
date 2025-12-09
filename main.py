#Truthy and Falsy

is_old = "hello"
is_licenced = 10

print(bool(is_old))
print(bool(is_licenced))
# python will convert is_old to True and is_licenced to True
#There are some values that python will convert to False, like 0, None, "", [], {}, ()
is_licenced = None
is_old = ""
print(bool(is_old))
print(bool(is_licenced))
if is_old and is_licenced:
   print("you are old enough to drive, and you have a licence!")
else:
   print("you are not of age!")

#Below  is a trick to check if a variable is empty or not

password = "123"
username = "joe"

if password and username:
   print("you are logged in!")
   print(f"your username is {username} and your password is {password}"
        )
else:
   print("you must provide username and password")
   print(f"your username is {username} and your password is {password}")

# This was truthy and falsy vaules helpeful for us to check if a variable is empty or not


# Ternary Operator
# just clean or short hand way to write if else statement
# condition_if_true if condition else condition_if_else
is_friend = True
can_message = "message allowed" if is_friend else "not allowed to message"
print(can_message)


# Logical Operators

is_magician = True
is_expert = True

# check if magician and expert,"you are a master magician"
if is_magician and is_expert:
   print("you are a master magician")
   # check if magician but not expert,"at least you're getting there"
elif  is_magician and not is_expert:
   print("at least you're getting there")
   # if you're not a magician:"you need magic powers"
elif  not is_magician:
   print("you need magic powers")

  #Loops 
  #range

for item in range(10):
   print(item)
 #range us just kike range in golang

for _ in range(10):
   print(_)   # _ is a convention for unused variables just like _ in golang
for _ in range(0, 10, 2):
   print(_)

# quick trick to reverse a string
# ascending order or descending order

for _ in range(10, 0, -1):
   print(_)

for  _ in range(10, 0): # this will not work like above because the step is positive and the start is greater than the end
   print(_)

# quick way to create a list of numbers
for _ in range(2):
 print(list(range(10)))

  # enumerate
   # enumerate is a built in function that returns an enumerate object 
   # enumerate object is an iterator that produces pairs of index and value

     # enumerate is useful when you want to get the index and the value of a list or a string

for  i, char in enumerate( [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
   print(i, char)
    # exerise
for  i, char in enumerate(list(range(100))):
       if char  == 50:
          print(f"index of 50 is {i}")
