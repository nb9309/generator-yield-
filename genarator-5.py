def fun3(start,stop,step):
    while start < stop:
        yield start
        start += step


a = fun3(int(input('enter start value: ')),int(input('enter stop value: ')),int(input('enter step value: ')))
print(next(a))
for val in a:
    print(val)