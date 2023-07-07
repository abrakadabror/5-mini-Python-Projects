import random

user_wins = 0 
computer_wins = 0
options = ['rock', 'paper', 'scissors']

while True:
    user_input = str(input('Type Rock/Paper/Scissors or Q to quit: ').lower()) #user podaje q - koniec programu
    if user_input == 'q':
        break
    if user_input not in options: #jesli uzytkownik poda powyzsze slowa kontunujey i wracamy do poczatku petli while
        continue

    random_number = random.randint(0, 2) #zakres 
    # rock 0, paper: 1, scissors: 2
    computer_pick = options[random_number] #wybor komputera
    print('Computer picked', computer_pick + '.')

    if user_input == 'rock' and computer_pick == 'scissors': #sprawdzamy czy warunek po lewej stronie jest rowny warunkowi po prawej, jest oba sa rowne to wtedy jest ok
        print('You won!') #wyswietli you won jesli oba warunki sa rowne sobie 
        user_wins += 1
        continue
    if user_input == 'paper' and computer_pick == 'rock': #sprawdzamy czy warunek po lewej stronie jest rowny warunkowi po prawej, jest oba sa rowne to wtedy jest ok
        print('You won!') #wyswietli you won jesli oba warunki sa rowne sobie 
        user_wins += 1
        continue
    if user_input == 'scissors' and computer_pick == 'paper': #sprawdzamy czy warunek po lewej stronie jest rowny warunkowi po prawej, jest oba sa rowne to wtedy jest ok
        print('You won!') #wyswietli you won jesli oba warunki sa rowne sobie 
        user_wins += 1
        continue
print('Goodbye!')

