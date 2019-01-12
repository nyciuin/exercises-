allGuests = {
    'Alice' : {'apples' : 1 , 'eggs' : 3 , 'carrots' : 2} , 
    'Bob'   : {'oranges' : 5 , 'apples' : 2 , 'melons' : 1} , 
    'Carol' : {'bananas' : 3 , 'eggs' : 4 , 'melons' : 1}
}

def totalItems(guest, item):
    nItem = 0
    for k, v in guest.items():
        nItem = nItem + v.get(item, 0)
    return nItem

print('total number of things:')
print(' - apples           ' + str(totalItems(allGuests, 'apples')))
print(' - eggs             ' + str(totalItems(allGuests, 'eggs')))
print(' - carrots          ' + str(totalItems(allGuests, 'carrots')))
print(' - oranges          ' + str(totalItems(allGuests, 'oranges')))
print(' - melons           ' + str(totalItems(allGuests, 'melons')))
print(' - bananas          ' + str(totalItems(allGuests, 'bananas')))