def fun1(num):
    n = 0
    while n<num:
        yield n
        n = n+1

a = fun1(int(input('enter value: ')))
while 9:
    try:
        print(next(a))
    except StopIteration:
        break