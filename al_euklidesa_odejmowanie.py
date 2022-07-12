# algorytm euklidesa odejmowanie
import random
a, b = random.randint(1000,50000),random.randint(1000,50000)
print("a = ",a,"\nb = ",b)
while a != b:
        if a > b:
                a -= b # --> a = a - b
        else :
                b -= a
print("NWD = ",a)
#32611
