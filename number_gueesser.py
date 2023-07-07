import random #domyslnie w pythonie 

#Sposob numer #1 do generowania liczb
# r = random.randrange(-5, 11) #(-1, 10) jesli chcesz zaczac generowac  od -1 i zakonczyc na 9
# print(r) 

#Sposob numer #2 do generowania liczb
# r = random.randint(-5, 11) #moze wygenerowac losowo rowniez 11 
# print(r)



top_of_range =  input('Type a number: ') #uzytkownik podaje numer

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <0:  #podana liczba przez uzytkownika musi byc wieksza od 0
        print('Please type a number larger than 0 next time')
        quit()
else:
    print('Please type a number next time.') #jesli nie jest wyswietl ten komunikat
    quit()
random_number = random.randint(0, top_of_range) #uzywamy top_of_range do generowania numerow
print(random_number) #drukujemy random_number z lini wyzej
