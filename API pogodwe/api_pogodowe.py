import requests
from requests import get
from json import loads # load z pliku znajdujacego sie na dysku, 'loads' odczytuje string
from terminaltables import AsciiTable 

CITIES = ['Gdańsk', 'Warszawa', 'Lublin', 'Wrocław', 'Rzeszów']




def main():
    url = 'https://danepubliczne.imgw.pl/api/data/synop'
    response = requests.get(url)
    rows = [['Miasto','Godzina pomiaru','Temperatura'
    ]]

    for row in loads(response.text):
        if row['stacja'] in CITIES:
            rows.append([
                row['stacja'],
                row['godzina_pomiaru'],
                row['temperatura'],
                row['cisnienie']
            ])
    table = AsciiTable(rows) #agrumentem jest teble data czyli rows w tym przypadku
    print(table.table)
if __name__ == '__main__':
    print('podgodynka 2023')
    main()