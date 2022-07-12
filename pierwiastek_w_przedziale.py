import math

def funkcja(x):
    y = 3*x**2 + 5*x - 7
    return y

epsx, epsy = 1e-16, 1e-16
p = -3
k = -2
wynik = False

fp = funkcja(p)
fk = funkcja(k)
fx0 = 0

if fp * fk > 0: print("Funkcja nie przecina osi w tym przedziale")
else:
    wynik = True
    while True :
        x0 = (p+k)/2
        if abs(p -x0)< epsx: break

        fx0 = funkcja(x0)

        if abs(fx0) < epsy : break

        if funkcja(p) * fx0 < 0: k = x0
        else:
            p = x0
            fp = fx0

if wynik : print(x0)
