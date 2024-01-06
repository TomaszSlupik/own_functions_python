#  zwrócenie maksimum z dwóch liczb.
def maximum(a, b):
    return max(a, b)

print(maximum(4, 2))
print(maximum(-4, 2))

print('---')

# zwrócenie maksimum z trzech liczb. W rozwiązaniu nie używaj funkcji max.

def maxOwn(a, b, c):
    numbers = [a, b, c]
    sortNumber = sorted(numbers)
    return sortNumber[-1]

print(maxOwn(4, 2, 1))
print(maxOwn(-3, 2, 5))

print('---')

# jako parametr przyjmie obiekt iterowalny (list, tuple) oraz zwróci iloczyn wszystkich elementów listy.
from functools import reduce

def multi(*args):
    return reduce(lambda x, y: x * y, args)

firstResult = (-4, 6, 2)
secondResult = ([4, 2, -5])

print(multi(*firstResult))
print(multi(*secondResult))

print('---')

# funkcja która przyjmie listę słów i zwróci długość najdłuższego słowa.
oneLongest = ['python', 'sql']
twoLongest = ['java', 'sql', 'r']


def map_longest(language):
    for num in sorted(language, key=len, reverse=True):
        return f"{len(num)}"

print(map_longest(oneLongest))
print(map_longest(twoLongest))

print('---')

# funckja która przyjmie listę słów i zwróci słowa o długości większej lub równej 6 znaków.

oneCheck = ['programowanie', 'python', 'java', 'sql']
twoCheck = ['java', 'sql']

def filter_ge_6(checkWord):
    for check in checkWord:
        if len(check) >= 6:
            return check
        else:
            return []
        
print(filter_ge_6(oneCheck))
print(filter_ge_6(twoCheck))

print('---')

