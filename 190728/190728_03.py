# dictionary == Hash .. Key & Value
# key 찾기 용이, key 중복 x

print("Dictionary")
print()

dic = dict(name="asd", num="010", etc="asd123")
print(dic)
dic[4] = "test"
print(dic)
print()

dic2 = {1: "a", 2: "b"}
dic2[3] = "c"
print(dic2)
del dic2[3]
print(dic2)
print(dic2[1])
print()

dic3 = {}

for i in dic2:
    print(i, dic2[i])

for i in range(1, 27):
    dic3[i] = chr(64 + i)

print(dic3)
print(dic3.keys())
print(dic3.values())
print(dic3.get(20))
print(2 in dic2)
