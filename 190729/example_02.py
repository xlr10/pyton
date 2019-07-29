###################### 01
import glob
import time

print()
print("example 01")


class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val


class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val


cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)  # 10에서 7을 뺀 3을 출력

###################### 02
print()
print("example 02")


class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value >= 100: self.value = 100


cal = MaxLimitCalculator()
cal.add(50)  # 50 더하기
cal.add(60)  # 60 더하기

print(cal.value)  # 100 출력

###################### 03
print()
print("example 03")

print(all([1, 2, abs(-3) - 3]))
print(chr(ord('a')) == 'a')

###################### 04
print()
print("example 04")
# lamda 함수결과값이 참인것들만 연산 후 묶어 리턴/ heap에서 동작
print(list(filter(lambda a: a > 0, [1, -2, 3, -5, 8, -3])))

###################### 05
print()
print("example 05")

print(hex(234))
print(int(0xea))

###################### 06
print()
print("example 06")
# map 함수결과값을 연산 후 묶어 리턴 / 게으른 연산으로 메모리절약
print(list(map(lambda a: a * 3, [1, 2, 3, 4])))

###################### 07
print()
print("example 07")
tmp = [-8, 2, 7, 5, -3, 5, 0, 1]
print(max(tmp), min(tmp))

###################### 08
print()
print("example 08")

print(round(17 / 3, 4))


###################### 11
print()
print("example 11")

print(glob.glob("D:\\Programming\\PYTHON\pyton\\190729\\*.py"))


###################### 12
print()
print("example 12")

print()

print(time.ctime())