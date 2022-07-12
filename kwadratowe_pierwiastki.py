w=1
while w > 0 :
        import math

        print("Wyliczam pierwiastki rzeczywiste rónania kwadratowego\n")

        a = float(input("Podaj a = "))

        if a == 0 :
                print("To równanie nie jest kwadratowe")
        else :
                b = float(input("Podaj b = "))
                c = float(input("Podaj c = "))


        delta = b**2-4*a*c
        if delta != 0 :
                x1 = (-b - (delta)**(1/2))/(2*a)
                x2 = (-b + (delta)**(1/2))/(2*a)
                print("x1 = ",x1)
                print("x2 = ",x2)
        #elif delta < 0 :
                #print("Nie ma Pierwiastków rzeczywistych\n")

        p=input("Czy chcesz znaleźć inne pierwiastki? (Tak lub Nie) ")
        if p == "Tak" or p=="tak" :
                w=1
        elif p!= "Tak" or p!="tak" :
                w=0
        
                

	
