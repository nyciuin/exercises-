
print('Please enter string:')
phrase = str(input())

vowelList = ['a', 'e', 'i', 'o', 'u']
vowels = 0

for e in phrase:
    if e in vowelList:
        vowels += 1

vowelPercent = (vowels / len(phrase)) * 100
print(str(vowelPercent) + '% vowels')