def test_execute():
    l1 = [10, 20, 30, 40]
    l2 = [98, 48, 43, 56]

    l3 = list(map(int, map(lambda x, y: x + y, l1, l2)))
    print(list(map(lambda x, y: x + y, l1, l2)))


def test_gen(index):
    weekdays = ['sun', 'mon', 'tue', 'wed', 'thr', 'fri', 'sat']
    yield weekdays[index]
    yield weekdays[index + 1]


def test_quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return test_quicksort(left) + middle + test_quicksort(right)


def test():
    s = input("Enter main string: ")
    subs = input("Enter sub string: ")
    pos = -1
    n = len(s)
    while True:
        pos = s.find(subs, pos + 1, n)
        if pos == -1:
            break
        print("Found at position ", pos)
        flag = True
        if flag == False:
            print("Not found")


def test_slicing():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    id_num = input("Enter ID num: ")
    if len(first_name) > 3 and len(last_name) > 3:
        first_name = first_name[:3]
        last_name = last_name[:3]
        id_num = id_num[- 3:]
        login_name = first_name + last_name + id_num
    else:
        login_name = first_name + last_name + id_num

    print(login_name)


def test_internal_content():
    s = "Ashlin Robinson Karkada"
    l = []

    for str in s.split():
        n = len(str) - 1
        target = ''
        while n >= 0:
            target += str[n]
            n -= 1
        l.append(target)
    print(l)


def test_identity_operators():
    a = ['durga']
    b = ['durga']
    print(id(a))
    print(id(b))


def sum_sub(a, b):
    sum = a + b
    sub = a - b
    return sum, sub


def factorial(n):
    if n == 0:
        result = 1
    else:
        result = n * factorial(n - 1)
    return result


def decor1(func):
    def inner(name):
        print("First Decor function execution")
        func(name)

    return inner


def decor2(func):
    def inner(name):
        print("Second Decor function execution")
        func(name)

    return inner


def find_execution_time(func):
    def inner(**kwargs):
        import time
        start_time = time.time()
        print("Function started at ", start_time)
        func(**kwargs)
        end_time = time.time()
        print("Function ended at ", end_time)

    return inner


@find_execution_time
def wellhello(a,b):
    print("hello {} , {} ".format(a,b))


@decor2
@decor1
def wish(name):
    print("Hello {0}!! Good Morning!!!".format(name))


def just_random(**kwargs):
    print(kwargs)


if __name__ == '__main__':
    pass
