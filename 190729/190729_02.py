# funtion input/ ouput
print("funtion input/ ouput")
print()

# print(input()) #echo

f = open("new file.txt", "w")
for i in range(0, 10):
    f.write(str(i) + '\n')

f.close()
print("end file")

f = open("new file.txt", "r")
# print(f.readlines())
# for i in f.read():
#     print(i,end="")

# while True:
#     line = f.readline()
#     if not line: break
#     print(line)

print(f.read())
f.close()

f = open("new file.txt", "a")
for i in range(2, 10):
    for j in range(2, 10):
        f.write("%2s" % str(i * j) + " ")
    f.write("\n")

f.close()

f = open("new file.txt", "r")
print(f.read())
f.close()
