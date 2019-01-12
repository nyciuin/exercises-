from collections import defaultdict
import pprint

fruitList = ['apple' , 'apple' , 'orange' , 'pear' , 'banana' , 'pear', 'melon', 'grape', 'melon', 'apple' , 'canteloupe' , 'orange' , 'banana' , 'nectarine' , 'plum' , 'orange']


newDict = defaultdict(int)

for k in fruitList:
    newDict[k] += 1

bag = {
    'keys' : 1 , 
    'wallet' : 1 , 
    'book' : 3 , 
    'foods' : 2
}

bagList = []
for k, v in bag.items():
    bagList = bag[k] * v
print(bagList)

# pprint.pprint(newDict)
