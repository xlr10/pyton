#example https://wikidocs.net/42526

###################### 01
print("example 01")
score = dict(kor = 80, eng = 75, math = 55)

avr = [0, 0]

for i in score :
    avr[0] += score.get(i)
    avr[1] += 1

avr[0] /= avr[1]

print("average : {aver}" .format(aver=avr[0]))

