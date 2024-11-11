def fun2(start,stop):

    while start<stop:
        yield start
        start += 1 


a = fun2(int(input('enter start value: ')),int(input('enter stop value: ')))
for val in a:
    print(val)
