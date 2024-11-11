# using next function
def fun1(num):
    n = 0
    while (n<num):
        yield n
        n=n+1


a = fun1(int(input('enter number: ')))
print('type of a is {}, type of fun1 is {}'.format(type(a),type(fun1)))
print(next(a))
print(next(a))
print(next(a))