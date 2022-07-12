print("Program kodujący napisy\n")
n=input("Podaj imie    ")

#kodowanie
kod=[]
for i in range(len(n)):
    x=(ord(n[i])+3)
    if x>122:
        x=x-97
    kod.append(x)
print("\n",kod)

