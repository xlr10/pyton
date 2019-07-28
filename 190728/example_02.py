# example https://wikidocs.net/42527


###################### 01
print()
print("example 01")

a = "Life is too short, you need python"

if "wife" in a:
    print("wife")
elif "python" in a and "you" not in a:
    print("python")
elif "shirt" not in a:
    print("shirt")
elif "need" in a:
    print("need")
else:
    print("none")

###################### 02
print()
print("example 02")

cnt = 0
result = 0

while cnt <= 1000:
    if cnt % 3 == 0:
        result += cnt
        print(result, cnt)
    cnt += 1

print(result)

###################### 03
print()
print("example 03")

i = 1

while i <= 5:
    for j in range(0, i):
        print("*", end=" ")
    i += 1
    print()



###################### 04
print()
print("example 04")

for i in range(1,101) :
    print(i, end=" ")
print()



###################### 05
print()
print("example 05")

class_a = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

aver = 0

for i in class_a :
    aver += i

aver /= len(class_a)

print(aver)



###################### 06
print()
print("example 06")

numbers = [1,2,3,4,5]
result2 =[i*2 for i in numbers if i%2 != 0]
print(result2)





