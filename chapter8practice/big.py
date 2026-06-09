def big(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
    
a = 45
b=4788
c= 455
print(big(a,b,c))
