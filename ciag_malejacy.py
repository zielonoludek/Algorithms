x=input("podaj liczbe   ")
y=0
for i in range(0,len(x)):
    if int(x[i]) % 2 == 0 :
        y+=1
if y== len(x):
    print("TAK")
else : print("NIE")
