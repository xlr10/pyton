# class
print("class")
print()


class FourCal:
    class_num = 1;

    def __init__(self, first, second):
        self.first = first
        self.second = second

    # def __init__(self, first, second):
    #     self.first = first
    #     self.second = second

    # def setNum(self, first, second):
    #     self.first = first
    #     self.second = second

    def add(self):
        return self.first + self.second

    def sub(self):
        return self.first - self.second

    def mul(self):
        return self.first * self.second

    def div(self):
        return self.first / self.second


test = FourCal(1, 4)
print(type(test))

# test.setNum(1,2)

print(test.add())
print(test.sub())
print(test.mul())
print(test.div())


class FourCal_pow(FourCal):
    def pow(self):
        return self.first ** self.second


test_inheritance = FourCal_pow(2, 3)

print(test_inheritance.add())
print(test_inheritance.sub())
print(test_inheritance.mul())
print(test_inheritance.div())
print(test_inheritance.pow())


class FourCal_safe(FourCal):
    def div(self):
        if self.second == 0:
            print("Can't Divide Zero")
            return 0
        else:
            return super().div()


test_override = FourCal_safe(2, 0)

print(test_override.add())
print(test_override.sub())
print(test_override.mul())
print(test_override.div())
