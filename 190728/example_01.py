# example https://wikidocs.net/42526


###################### 01
print("example 01")
score = dict(kor=80, eng=75, math=55)

# avr = [0, 0]
# for i in score :
#     avr[0] += score.get(i)
#     avr[1] += 1
# avr[0] /= avr[1]
# print("average : {aver}" .format(aver=avr[0]))

# refactoring
avr = dict(average=0, count=0)

for i in score:
    avr['average'] += score.get(i)
    avr['count'] += 1

avr['average'] /= avr['count']

print("average : {aver}".format(aver=avr['average']))



###################### 02
print()
print("example 02")
num = 13
if (num % 2) == 0:
    print("13 is even")
else:
    print("13 is odd")



###################### 03
print()
print("example 03")

social_code = "881120-1068234"

print("19{YY} {MM} {DD}".format(YY=social_code[:2], MM=social_code[2:4], DD=social_code[4:6]))



###################### 04
print()
print("example 04")

pin = "881120-1068234"

print("{gender}".format(gender=pin[7]))



###################### 05
print()
print("example 05")
a = "a:b:c:d"
print(a.replace(":", "#"))



###################### 06
print()
print("example 06")

list1 = [1, 3, 5, 4, 2]
list1.sort()
list1.reverse()
print(list1)



###################### 07
print()
print("example 07")

list2 = ['Life', 'is', 'too', 'short']

print(" ".join(list2))



###################### 08
print()
print("example 08")

tp1 = 1, 2, 3
tp2 = 4,
tp1 += tp2

print(tp1)



###################### 09
print()
print("example 09")

a = dict()
a['name'] = 'python'
print(a)



###################### 10
print()
print("example 10")

a2 = {'A': 90, 'B': 80, 'C': 70}

print(a2.pop('B'))



###################### 11
print()
print("example 11")

a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]

print(set(a))


