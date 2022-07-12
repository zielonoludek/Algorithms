print("Program do obliczania wartości wielomianu dla podanego argumentu wg Hornera \n")
n = int(input("podaj stopień wielomianu n= "))
x=float(input("podaj x "))
print("Podaj wartości wspóczynników a0, a[1], a[2], a[3] .... a[n]")
y=0
a=[]
for i in range(n+1):
    print("a",y)
    b= float(input("    a = "))
    a.append(b)
    y+=1
y=0
while n>=0:
    y=y*x+a[n]
    n-=1
print(y)
