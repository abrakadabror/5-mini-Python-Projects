#manadzer hasel
pwd = input('what is the master passowrd?')


def view():
    pass
def add():
    pass


while True: # gdy prawdziwe to
    mode = input('Wodul you like to add a new passowrd or view a existing ones(view, add, press q to quit)?')
    if mode == 'q': #przerywamy dzialanie programu
        break
    if mode == 'view': # jesli uzytkownik poda view
        view() #wywolujemy funckje view()
    elif mode == 'add': #jesli uzytkownik poda add
        add() #wywolujemy funkcje add()
    else: #jesli nie poda zadnego z powyzszych
        print('Invalid mode.')
        continue #wracamy na poczatek petli
