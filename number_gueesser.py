import random # biblioteka domyslnie w pythonie 

#Sposob numer #1 do generowania liczb
# r = random.randrange(-5, 11) #(-1, 10) jesli chcesz zaczac generowac  od -1 i zakonczyc na 9
# print(r) 

#Sposob numer #2 do generowania liczb
# r = random.randint(-5, 11) #moze wygenerowac losowo rowniez 11 
# print(r)
######### program |ZGADYWACZ|

top_of_range =  input('Type a number: ') #uzytkownik podaje numer
guesses = 0
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

while True:
    guesses += 1 #bedziemy zliaczac w tym miejsu ilosc prob uzytkownika potrzebnych do zgadniencia liczby
    user_guess = input('Make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.') #jesli nie jest wyswietl ten komunikat
        continue #sprowadza nas ponownie na start petli while
    if user_guess == random_number:
        print('You got it!')
        break #przerywamy break petle while
    # else:
    #     #print('You got it wrong') #zeby przerwac petle nieskonczona nalezy wcisnac crtl + c
    #     if user_guess > random_number: #dodanie linijki 39 informujacej uzytkownika, ze jego liczba byla powyzej lub ponizej wylosowanej
    #         print("You were above the number!")
    #     else:
    #         print('You were below the number!')

    elif user_guess > random_number:
        print('You were above the number!')
    else:
        print('You were below the number!')
    


print(f'You got it in:  {guesses}  Congratulations!') #sprawdzamy z f-stringiem w w ilu probach udalo sie zgadnac odpowiedz uztykownikowi
print('You got it', guesses, 'attempts') #sprawdzamy w ilu probach udalo sie zgadnac odpowiedz uztykownikowi