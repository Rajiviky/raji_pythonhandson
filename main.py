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