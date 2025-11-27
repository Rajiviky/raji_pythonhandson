# Dictiionary

dictionary = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
}

print(dictionary['a'])
print(dictionary['b'])
dictionary = [{
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
}, {
    'a': 5,
    'b': 6,
    'c': 3,
}]

print(dictionary[0]['a'])
print(dictionary[1]['a'])

# Dictionary keys

dicti = {
    123: [1, 2, 3],
    True: 'hello',
    #this will throw an error because keys must be immutable
    # [100]: True
}
print(dicti[123])

# Dictionary methods

user = {'basket': [1, 2, 3], 'greet': 'hello', 'age': 20}
# this will throw an error because the key does not exist
# print(user['name'])

# this will not throw an error, though the key does not exist
print(user.get('name'))

# this will not throw an error and will return the default value

print(user.get('name', 'user'))

# We can create a dictionary this way, but it's not very common

user2 = dict(name='JohnJohn')

print(user2)

# check if a key exists in a dictionary , returns True or False
print('basket' in user)
print('size' in user)

print('age' in user.keys())
print('hello' in user.values())

# print all the keys in a dictionary

print(user.keys())

# print all the values in a dictionary

print(user.values())

# print all the items in a dictionary

print(user.items())  # returns a list of tuples , which will learn later

# copy a dictionary

user2 = user.copy()
print(user2)

# clear a dictionary

user.clear()
print(user)

# this will not clear user2 because it's a copy of user
print(user2)

print(user2.pop('age'))

# this will remove the age item in the dictionary
print(user2)

# this will remove randomly an item in the dictionary
print(user2.popitem())
print(user2)

# update a dictionary

user2.update({'age': 55})

print(user2)

# even  if the key does not exist, it will add it to the dictionary

user2.update({'ages': 55})

print(user2)

# Tuple

# Tuple is a data structure like list, but it's immutable

my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
 # this will throw an error because tuple is immutable
# my_tuple[1] = 'z'

print(my_tuple[1])

# we cannot perform any methods on tuple that will change it, like append, insert, extend, pop, remove, clear, sort, reverse, etc.     # but we can perform methods that will not change it, like count, index, etc.

# then why do we need tuple? because tuple is faster than list, and it's used when we don't want to change the data. Example developer can use tuple whne he wants to make sure that the data will not be changed by mistake.

# Example scenerio , google  maps api, it returns a tuple of latitude and longitude, and we don't want to change it by mistake.

# tuple has 2 methods, count and index

print(my_tuple.count(1))
print(my_tuple.index(1))

#set 
# set is a data structure that is unordered and does not allow duplicates

my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(my_set)

my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10}
# this will remove the duplicates, only unique values will be kept

print(my_set)

my_set.add(100)
my_set.add(2)
print(my_set)
# this will not add 2 because it's already in the set

my_list = [1,2,3,4,5,5,6]
# this will remove the duplicates, only unique values will be kept
print(set(my_list))

# example we have list of user names and emails  and we want to remove the duplicates. this  is a common use case for set

# below will throw an error becs we cannot access set by index
# print(my_set[0])
# we can check if an item is in the set by "in" keyword  "
print(1 in my_set)
print(10 in my_set)

# count only unique values
print(len(my_set))

# convert set to list
print(list(my_set))
          
