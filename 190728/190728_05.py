#for

####
marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60:
        continue

for i in range(2,10):
    for j in range(2,10):
        print("%2d" %(i*j), end=" ")
    print()
print()

tmp = [1,2,3,4]
result =[]
result= [n*3 for n in tmp if n%2==0]
print(result)

multi=[]
multi = [i*j for i in range(2, 10)
         for j in range(2, 10)]
#print(multi)
print([i*j for i in range(2, 10) for j in range(2, 10)])