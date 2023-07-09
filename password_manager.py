import cryptography
from cryptography.fernet import Fernet #nie pobiera cryptography....

master_pwd = input('what is the master passowrd?')
def write_key():
    key = Fernet.generate_key() #oznaczamy czym jest klucz 
    with open('key.key', 'wb') as key_file: # otwiera pik, tworzy plik on nazwie key.key w trynie wb i oznacza jako key_file
        key_file.write(key)

def view():
     with open('password.txt', 'r') as f: #  r - tylko odczyt,
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split('|') #dzielimy split zawsze gdy znajdzie znak '|'
            print('User:', user, ', Password', passw)
def add():
    name = input('Account name: ') #user podaje nazwe konta
    pwd = input('Password: ') #user podaje haslo

    with open('password.txt', 'a') as f: # w oznacza, napisywanie pliku, r - tylko odczyt, a - dodaje cos na koncu pliku i tworzy nowy plik jesli nie istneije.
        f.write(name + '|' + pwd + '\n') #pobieramy 'name' przedzielamy '|' oraz dodajemy 'password'

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
