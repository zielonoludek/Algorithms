n=int(input('Podaj liczbe  '))
def wartosc_bezwzgledna(x):
    if n < 0: wartosc_bezwzgledna = -n
    else : wartosc_bezwzgledna = n
    return wartosc_bezwzgledna
print(wartosc_bezwzgledna(n))
