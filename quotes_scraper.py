import requests
from bs4 import BeautifulSoup
import pandas as pd

all_quotes = []
url = 'http://quotes.toscrape.com/page/1/'

while url:
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    quotes = soup.find_all('div', class_='quote')
    
    for quote in quotes:
        text = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text
        tags = [tag.text for tag in quote.find_all('a', class_='tag')]
        all_quotes.append({'Text': text, 'Author': author, 'Tags': ', '.join(tags)})

    next_page = soup.find('li', class_='next')
    url = f"http://quotes.toscrape.com{next_page.a['href']}" if next_page else None

df = pd.DataFrame(all_quotes)
df.to_csv('quotes.csv', index=False)
print("Scraping Done!")
