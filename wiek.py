ur,teraz = int(input('Rok urodzenia  ')) ,int(input('Rok aktualny  '))

def wiek(ur,teraz):
    wiek = teraz - ur
    if wiek >= 120 :
        return 'Jesteś wampirem'
    if wiek >= 18 :
        return wiek, "DOROSŁY"
    else:
        return wiek,'NIEDOROSŁY'
    
print(wiek(ur, teraz))
