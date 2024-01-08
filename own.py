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

# funkcja, która zwróci liczbę obiektów typu str w obiekcie iterowalnym (list, tuple, set)

firstStr = ['p', 2, 4.3, None]
secondStr = {'p', 2, 4.3, True, 'True', None}

def count_str (myStr):
    total = 0
    for checkStr in myStr:
        if isinstance(checkStr, str):
            total += 1
    return total

print(count_str(firstStr)) 
print(count_str(secondStr))

print('---')

# funkcja która zwróci liczbę obiektów typu str o długości powyżej 2 znaków w obiekcie iterowalnym (lista, tuple, set)
thirdStr = [1, '#hello', '', 'python', 'go']
fourthStr = [1, 2, 3, 'python']

def count_strNext(check):
    total = 0
    for myString in check:
        if isinstance(myString, str):
                total += 1
    if total > 2:
         return total
    else:
        return f"Brak liczby obiektów typu str o długości powyżej 2 znaków w obiekcie iterowalnym"
    
print(count_strNext(thirdStr))
print(count_strNext(fourthStr))

print('---')

# funkcja remove_duplicates(), która usunie duplikaty z listy (kolejność elementów nie musi być zachowana).
one_duple = [1, 5, 3, 2, 2, 4, 2, 4]
two_duple = [1, 1, 1, 1]


def remove_duplicates(inputList):
     uniqueList = list(set(inputList))
     return uniqueList

print(remove_duplicates(one_duple))
print(remove_duplicates(two_duple))

print('---')

# funkcja is_distinct(), która sprawdzi, czy lista zawiera unikalne wartości.
# Użyłem porównania długości listy z długością zbioru które są unikalne zawsze
isUniqueListOne = [1, 2, 3]
isUniqueListTwo = [1, 2, 3, 3]

def is_distinct(isUnique):
    return len (isUnique) == len(set(isUnique))

print(is_distinct(isUniqueListOne))
print(is_distinct(isUniqueListTwo))

print('---')

kayak = 'kajak'
ocean = 'ocena'

def is_palindrome(strText):
    check_text = [check for check in strText]
    return check_text == check_text.reverse()

is_palindrome(kayak)
is_palindrome(ocean)

