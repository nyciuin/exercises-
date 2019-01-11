
cat = {'colour' : 'white', 'age' : 12, 'legs' : 4}

# keys, category needing a value
for k in cat.keys():
    print(k)
print('\n')

# values, attribute of a key
for v in cat.values():
    print(v)
print('\n')


# items, key/value pair

for i in cat.items():
    print(i)
print('\n')


# lists from a dictionary

print(cat.keys())
catKeyList = list(cat.keys())
print(catKeyList)

for k, v in cat.items():
    print('Key: ' + str(k) + ', Value: ' +str(v))
print('\n')


# get()ing stuff
# get(key, failsafe)

print('My cat has ' + str(cat.get('legs', 0)) + ' legs')
print('My cat has ' + str(cat.get('horns', 0)) + ' horns')
print('\n')


# setdefault

# if 'eye colour' not in cat:
#     cat['eye colour'] = 'yellow'

cat.setdefault('eye colour', 'yellow')
print(cat['eye colour'])
# no 'eye colour' exists already, added with a default
cat.setdefault('eye colour', 'green')
print(cat['eye colour'])
# 'eye colour' already exists, returns defualt value
print('\n')

sentence = 'the quick brown fox jumped over the lazy dog'
count = {}
for letter in sentence:
    count.setdefault(letter, 0)
    count[letter] = count[letter] + 1

import pprint       # allows better formatting of dictionaries
pprint.pprint(count)

