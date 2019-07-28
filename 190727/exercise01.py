print("hello pyton")
print("hello Github")
a = 3

if a > 1:
    print("a>2")
else:
    print("a<2")

for a in [1, 2, 3]:
    print(a)

b = 0
while b < 3:
    b = b + 1
    print(b)


def add(a, b):
    return a + b


print(add(2, 5))

c = 0o177
d = 0xfff

print(c, d, c**d)

multiLine = """pyton
is
easy"""

print(multiLine, len(multiLine), multiLine[2])
print(multiLine[0:5])
print(multiLine[0:])
print(multiLine[:15])

print("=" * 30)
print("PyCharm string exercise")
print("=" * 30)

e = 10
# 2개이상 포맷팅 %(param1, param2)
print("now %d%% %d%%" %(e, 3))

print("asd {0:<10} asd {1:-^10}".format("asd",2))
print( "here: {here:-^10}\nthere: {there}".format(here=1,there="asd"))

print(multiLine.upper())