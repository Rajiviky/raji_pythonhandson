# Dictiionary

dictionary = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
}

print(dictionary['a'])
print(dictionary['b'])
dictionary  = [
  {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
  },
  {
    'a': 5,
    'b': 6,
    'c': 3,
    
  }
]

print(dictionary[0]['a'])
print(dictionary[1]['a'])

# Dictionary keys

dicti  = {
    123: [1, 2, 3],
    True: 'hello',
  #this will throw an error because keys must be immutable
    # [100]: True
  
}
print(dicti[123])

# Dictionary methods

user = {
    'basket': [1, 2, 3],
    'greet': 'hello',
    'age': 20
  
}
# this will throw an error because the key does not exist
# print(user['name'])

# this will not throw an error, though the key does not exist
print(user.get('name'))

# this will not throw an error and will return the default value

print  (user.get('name', 'user'))

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

print(user.items()) # returns a list of tuples , which will learn later

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