import requests
from bs4 import BeautifulSoup
import pandas as pd

#| user_login='62177797'
#| url=f'https://www.kinopoisk.ru/user/{user_login}/votes/list/vs/vote/page/1/#list'
#| r=requests.get(url)
#| html_content = requests.get(url).text
#| with open('kinopoisk.html', 'w', encoding='utf-8') as output_file:
#|     output_file.write(r.text)
#|     soup = BeautifulSoup(r.text, 'lxml')
#|     entries = soup.find_all('div', class_='item')
#| print(len(entries))
#| data = []
#| for entry in entries:
#|    div_name_rus = entry.find('div', class_='nameRus')
#|    film_name = div_name_rus.find('a').text
#|    rating_film = entry.find('div', class_='vote').text
#|    data.append({'film name': film_name, 'Rating film': rating_film})
#| print(data)

def collect_user_rates(user_login):
    page_num = 1
    data = []
    while True:
        url = f'https://www.kinopoisk.ru/user/{user_login}/votes/list/vs/vote/page/{page_num}/#list'
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, 'lxml')
        entries = soup.find_all('div', class_='item')
        if len(entries) == 0:
            break
        for entry in entries:
            div_name_rus = entry.find('div', class_='nameRus')
            film_name = div_name_rus.find('a').text
            rating_film = entry.find('div', class_='vote').text
            data.append({'film name': film_name, 'Rating film': rating_film})
        page_num += 1
    return data
user_rates = collect_user_rates(user_login='62177797')
df = pd.DataFrame(user_rates)
df.to_excel('user_rates.xlsx')