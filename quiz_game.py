print('Welcome to my computer quiz!')

playing = input('Do you want to play?')

if playing != str('yes'):
    print('User refused to continue')
    quit()
print("Okay! Let's play:)")

answer = input('What does CPD stand for? ')
if answer == 'counting digits' or 'Counting Digits':
    print('Thats correct answer')
else:
    print('thats wrong answer')