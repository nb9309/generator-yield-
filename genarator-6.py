def fun(start,stop=0,step=1):
    if start > stop:
        stop = start
        start = 0
    while start<stop:
        yield start
        start += step

a = fun(int(input('enter start value: ')),int(input('enter stop value: ')),int(input('enter step value: ')))
for val in a:
    print(val,end=' ')
print()
a = fun(int(input('enter start value: ')),int(input('enter stop value: ')))
for val in a:
    print(val,end=' ')
print()
a = fun(int(input('enter stop value: ')))
for val in a:
    print(val,end=' ')
print()