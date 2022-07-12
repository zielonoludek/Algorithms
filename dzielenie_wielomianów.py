n = int(input("podaj stopień wielomianu n= "))
print("Podaj wartości wspóczynników a0, a[1], a[2], a[3] .... a[n]")
y=0
a=[]
for i in range(n+1):
    print("a",y)
    b= float(input("    a = "))
    a.append(b)
    y+=1
k=n
y=0
c=0
x = -100    
for i in range(len(a)):
    while x<100:
        c+=1
        if c == len(a):
            n=k
        y= y+(a[n]*x**n)
        n-=1
        x+=1
        c+=1
    if y==0:
        print("f(x)= 0 dla x=",x)
    

