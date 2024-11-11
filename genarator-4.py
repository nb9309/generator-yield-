def fun3(start,stop,step):
    for i in range(start,stop,step):
        yield i


a = fun3(int(input('enter start value: ')),int(input('enter stop value: ')),int(input('enter step value: ')))
print(next(a))
for val in a:
    print(val)