###################### 01
print()
print("example 01")


def is_odd(num):
    if num % 2 == 1:
        print("%d is Odd" % num)
    else:
        print("%d is Even" % num)


is_odd(1)
is_odd(2)

###################### 02
print()
print("example 02")


def average_serial(*args):
    result = 0

    for i in args:
        result += i

    result /= len(args)
    return result


print(average_serial(1, 2, 3, 4, 5, 6))


###################### 03
print()
print("example 03")
# input1 = input("Press 1st Number:")
# input2 = input("Press 2nd Number:")

#total = int(input1) + int(input2)

#print("Sum is %s " % total)


###################### 04
print()
print("example 04")

print("you" "need" "python")
print("you" + "need" + "python")
print("you", "need", "python")
print("".join(["you", "need", "python"]))


###################### 05
print()
print("example 05")

f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", 'r')
print(f2.read())
f2.close()


###################### 06
print()
print("example 06")

f1 = open("test2.txt", 'w')
#f1.write(input())
f1.close()

f2 = open("test2.txt", 'r')
print(f2.read())
f2.close()


###################### 07
print()
print("example 07")

f1 = open("test3.txt", 'r')
tmp=f1.read()
f1.close()
print(tmp)

print(tmp.replace('java','python'))

f1 = open("test3.txt", 'w')
f1.write(tmp.replace('java','python'))
f1.close()



