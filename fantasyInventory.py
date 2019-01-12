
# dictionary for player inventory items/quantities
# display inventory in a readable format

inventory = {
    'potion' : 10 ,
    'paintball' : 42 ,
    'mega potion' : 6 ,
    'gold' :21
}

def displayInventory(input):
    print('inventory currently contains:')
    itemTotal = 0
    for k, v in input.items():
        print(str(v) + ' ' + str(k))
        itemTotal = itemTotal + v
    print('Inventory space : ' + str(itemTotal) + '/100.')
    if itemTotal > 100:
        print('Your item bag is full!')
    print('\n')

displayInventory(inventory)


# list of new items
# add list to existing items
# display new dictionary of all items

from collections import defaultdict
import pprint

def dictMerge(d1, d2):
    mergedDict = {}

    for k in d1:
        if k in d2:
            newK = d1[k] + d2[k]
        else:
            newK = d1[k]
        
        mergedDict[k] = newK
    
    for k in d2:
        if k not in mergedDict:
            mergedDict[k] = d2[k]
    
    return mergedDict


def addToInventory(inventory, added):
    addedItems = {}
    for k in added:
        addedItems.setdefault(k, 0)
        addedItems[k] += 1


    newInventory = dictMerge(inventory, addedItems)

    return newInventory


carves = ['carapace' , 'carapace' , 'wing' , 'ruby' , 'gold' , 'gold' , 'gold']
inventory = addToInventory(inventory, carves)
displayInventory(inventory)