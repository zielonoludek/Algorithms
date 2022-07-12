x=0
def funkcja(x):
    funkcja= x/(x**2 +1)
    return funkcja

while x<= 10:
    print(round(x,3),'    ', round(funkcja(x),3))
    x+= 0.2
