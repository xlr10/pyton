# funtion

print("funtion")
print()


def add(a, b):
    return a + b


a = 1
b = 2
print(add(a, b))


def add_serial(*args):
    result = 0
    for i in args:
        result += i
    return result


print(add_serial(1, 2, 3, 4, 5))


def print_dic(**kwargs):
    print(kwargs)


print_dic(d=1)
print_dic(name='a', pss=123)


# 다수 parameter + 다수 return
def calcu(*args):
    result = {'add': 0, 'sub': 0, 'mul': 1, 'div': 1}

    for i in args:
        result['add'] += i
        result['sub'] -= i
        result['mul'] *= i
        result['div'] /= i

    return result


print(calcu(1, 2, 3, 4, 5))

add_lamda = lambda a, b: a + b
print(add_lamda(1, 2))
