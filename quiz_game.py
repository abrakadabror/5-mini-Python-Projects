print('Welcome to my computer quiz!')

playing = input('Do you want to play?')

if playing != str('yes'):
    print('User refused to continue')
    quit()
print("Okay! Let's play:)")

answer = input('What does CPD stand for? ')
if answer == 'counting digits':
    print('Thats correct answer')
else:
    print('thats wrong answer')

answer = input('What is wrong with you ')
if answer == 'everything is fine':
    print('Thats correct answer')
else:
    print('thats wrong answer')

answer = input('Why are you sleeping? ')
if answer == 'im not sleeping':
    print('Thats correct answer')
else:
    print('thats wrong answer')