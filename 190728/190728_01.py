# List == array

print("hello pyton")

list = [1, 2, 3]
list2 = [1, 2, [3, 4]]

print(list)
print(list2)
print(list2[2][1])
print(list2[0:2])
print(list * 3, len(list))
print()

del list[1]
print(list)
print("{list:-<10}".format(list=list[0]))
print("{list:-^10}".format(list=list[0]))
print("{list:->10}".format(list=list[0]))
print()

print(list.pop())
list.append(2)
list.append(3)
print(list)
list.reverse()
print(list)
print()

list += list
print(list, list.count(1))
list2.extend(list)
print(list2)
