def szukaj_bin(A):
    global prawy
    lewy,prawy=1,n
    while lewy<prawy:
        srodkowy=(lewy+prawy)//2
        if A[srodkowy]%2!=0:
            lewy=srodkowy+1
        else:
            prawy=srodkowy
    return prawy
