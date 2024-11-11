def fun(n):
    for i in range(n):
        return i,i+1,i+2


# main function
a = fun(int(input('enter number: ')))
print(a)