# set
# 중복, 순서 x
from copy import copy

print("Set")
print()

set1 = set("hello")
print(set1)

tu1 = tuple(set1)
print(tu1, tu1[0], tu1[2])

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1 & s2)
print(s1 | s2)
print(s1 - s2)

# bool
b1 = [1, 2, 3, 4]
while b1:
    print(b1.pop())

b2 = copy(b1)
print(b2 is b1)

set2 = set("asd")
# swap
set1, set2 = set2, set1
print(set1)
