# module1

# print(__name__)

def add(a, b):
    return a + b


def add_serial(*args):
    result = 0
    for i in args:
        result += i
    return result


def print_dic(**kwargs):
    print(kwargs)


# 다수 parameter + 다수 return
def calcu(*args):
    result = {'add': 0, 'sub': 0, 'mul': 1, 'div': 1}

    for i in args:
        result['add'] += i
        result['sub'] -= i
        result['mul'] *= i
        result['div'] /= i

    return result
