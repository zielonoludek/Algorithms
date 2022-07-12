m=1
while m==1:
    n=[]
    for i in range(5):
        x= int(input("podaj liczbe całkowitą   "))
        if  (type(x) != int):
            print("podaj inną liczbę")
            x=int(input("podaj liczbe całkowitą  "))
        n.append(x)

    najwieksze=n[0]
    najmniejsze=n[0]

    for i in range(5):
        if n[i] >= najwieksze:
            najwieksze = n[i]
        if n[i] <= najmniejsze:
            najmniejsze = n[i]

    print("Wartość najmniejsza:   ",najmniejsze)
    print("Wartość największa:   ", najwieksze)

    b=(input("Czychesz podać kolejne liczby ?   "))
    if (b=="tak") or (b=="TAK") or (b=="Tak"):
        m=1
    else: m=0
