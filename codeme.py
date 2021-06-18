import requests
from bs4 import BeautifulSoup


html_text = requests.get('https://www.keepinspiring.me/inspirational-words-of-encouragement/').text
soup = BeautifulSoup(html_text, 'lxml')
div= soup.find_all('h2')[:4]
for index, title in enumerate(div):
    title = title.text

quotes0 = soup.find_all('ul')
for index, quote in enumerate(quotes0[4:8]):
    quote = quote.text.replace('.', '.\n-')
    with open(f'quotes/{index}', 'w') as f:
        f.write(quote)
    print(f'file saved: {index}')

