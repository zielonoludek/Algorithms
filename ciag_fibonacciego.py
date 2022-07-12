def ciag(n):
    if n == 1 or n == 2:
        return(1)
    return (ciag(n-1)+ ciag(n-2))


a = int(input("Podaj liczba naturalna : "))
print(ciag(a))
