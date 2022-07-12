a=1
while a > 0 :
    print("Program wyliczający Twoje wynagrodzenie netto\n")

    b = float(input("Podaj swoje wynagrodzenie brutto (w złotókach) = "))

    def netto():
        global n
        global p
        n = b - p 
        print("\nTwój podatek do zapłaty wynosi ",round(p,2),\
          "zł. Na rękę otrzymasz ", round(n,2),"zł")

    
    if b < 0 :
        print("Podaj kwotę większą od zera\n")
        b = float(input("\n Podaj swoje wynagrodzenie brutto (w złotówkach) = "))
    elif b <= 3091.0 :
        print("\nNie płacisz podatku dochodowego")
    elif b <=44490 :
        p = b*0.19 - 586.85
        netto()
    elif b <= 85528:
        p = (b - 44490)*0.3 + 7866.25
        netto()
    elif b > 85528 :
        p = (b-88528)*0.4 + 20177.65
        netto()





    
    
    
    
    
