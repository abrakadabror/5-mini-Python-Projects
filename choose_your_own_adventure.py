name = input('type ypur name: ')
print('Welcome', name, 'to this adventure!')

answer = input('You are on a dirty road, it has come to an end and you can go let or right. Which way woudl like to go?').lower() #zadajemy pytanie 
if answer == 'left': #jesli odpowiedz to w lewo 
    answer = input("You come to a river, you can walk around or swim across? Type walk to walk around and swim to siwm accreoss") # to zadajemy pytanie
    if answer == 'swim': #sprawdzamy w if jaka jest odpowiedz na powyzsze pytanie,  jesli odpowiedz to swim to nic nie "wydrukuje"
        print(' You swam across and were eaten by aligator.')
    elif answer =='walk': #jesli odpowiedz to walk 
        print('You walked for many miles, ran out of water and you lose a game')
    else:
        print('Not a valid option.You lose.')
elif answer == 'right':
    answer = input("You come to a bridge. It's looks woobly, do you want to cross it?")
    if answer == 'back':
         print('You were kicked in the ass by a human-tourch')
    elif answer =='cross':
        print('You walked for many miles, ran out of water and you lost the game')
    else: 
        print('Not a valid option. You lose.')
else:
    print('Not a valid option.You lose.')
