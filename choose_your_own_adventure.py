name = input('type ypur name: ')
print('Welcome', name, 'to this adventure!')

answer = input('You are on a dirty road, it has come to an end and you can go let or right. Which way woudl like to go?').lower() #zadajemy pytanie 
if answer == 'left': #jesli odpowiedz to w lewo 
    answer = input("You come to a river, you can walk around or swim across? Type walk to walk around and swim to siwm accreoss") # to zadajemy pytanie
    if answer == 'swim': #sprawdzamy w if jaka jest odpowiedz na powyzsze pytanie,  jesli odpowiedz to swim to nic nie "wydrukuje"
        print()
    elif answer =='walk': #jesli odpowiedz to walk 
        print()
    else:
        print('Not a valid option.You lose.')
elif answer == 'right':
    print()
else:
    print('Not a valid option.You lose.')
