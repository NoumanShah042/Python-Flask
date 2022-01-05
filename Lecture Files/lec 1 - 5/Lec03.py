def some1():
    return "Hello"


def some2():
    print("Hello")


help(some1())
help("list")

res1 = some1()
res2 = some2()
# NULL
# None
print(res1)
print(res2)
# These four basic collections
# list
# dictionary
# set
# tuple


# start with list
# List items are ordered, changeable, and allow duplicate values.

numbers = [1, 2, 3, 4, 5, 6]
names = ["Ali", "Ahmed", "Aisha", "Amna"]
print(type(numbers))
print(len(numbers))
print(type(names))
print(len(names))
numbers.append(7)
for n in numbers:
    print(n)
n = numbers.pop()
print(n)
for n in numbers:
    print(n)
numbers.pop()
for n in numbers:
    print(n)
print("second index", numbers[2])
numbers.append(99)
numbers.append(89)
numbers[2] = 30
print(type(numbers[2]))
for n in numbers:
    print(n)
numbers.sort()
for n in numbers:
    print(n)

mix = ["hello", "one", 1, 3.5]

# Tuple is collection which is ordered and unchangeable
t = (1, 2, 3, 3)
another = ("one", "two", "three", "three")
for elment in t:
    print(elment)
tup = ("one", 1, "two", "three")
print(tup[0])
# tup[0]="onnnnn"
print(tup[0])

# A set is a collection which is both unordered and unindexed.
# Set items are unordered, unchangeable, and do not allow duplicate values.
someset1 = {1, 2, 3, 4, 5}
someset2 = {"one", "two", "three", "three"}
for s in someset1:
    print(s)
for s in someset2:
    print(s)
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
testDic = {"key1": 0, "key1": 1, "key2": 2, "k3": 3}
print("Dictionary length", len(testDic))
print(testDic["key1"])
print(testDic["k3"])
testDic["k3"] = 53
# Adding new element ujsing update method
testDic.update(k4=123)
# Adding new element in dictionary
testDic["k5"] = 556443
testDic.update(k5=56)
# removing an element from dictionary
testDic.pop("key1")
keyslist = testDic.keys()
print(type(keyslist))
for key in keyslist:
    print(testDic[key])
testDic.clear()
for key, value in testDic.items():
    print(key, value)
list1 = [1, 2, 3, 4]
list2 = ["one", "two", "three"]
list3 = ["aik", "do", "teen", "four"]
print("zipped :", type(zip(list1, list2, list3)))
zipped = zip(list1, list2, list3)
print(tuple(zipped))

for l1, l2, l3 in zip(list1, list2, list3):
    print(l1, l2, l3)
