def fun(start,stop=0,step=1):
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