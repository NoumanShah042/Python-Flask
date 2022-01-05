import math as m

print(type(m.sqrt(4)))
# int ,float , number , string , boolean , tuple -> immutable
# list , set , dictionary    -> mutable
# ************************

var = 10
print(type(var))
var1 = 1.5
print(type(var1))
print("memory address of var", id(var))


def myfunction1(v):
    print("memory address of v", id(v))
    v = v * 2 * 3
    print("memory address of v", id(v))
    print("print from function", v)
    return v


myfunction1(var)
print("print after function", var)
print("memory address of var", id(var))

# ************************

list_ = [1, 2, 3, 4]


def myfunction2(l):
    l[3] = l[3] + 10
    l.append(4)


for l in list_:
    print(l)
myfunction2(list_)
print(list_[3])


# set_={1,2,3}
# set_2 = set(1,2,3)
# myfunction2(set_)

for l in list_:
    print(l)

listtt = [1, 2, 3]
listt2 = list(listtt)

for i in listtt:
    print("item type", type(i))
for i in listt2:
    print("i typ:", type(i))
# listt2[0]=444
# print(listtt,listt2,sep="\n")
# print(id(listtt),id(listt2))
