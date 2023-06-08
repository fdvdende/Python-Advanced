import requests
import bs4
import sys

url = input('Geef url: ')
if not url.lower().startswith('http'):
    url = 'http://' + url

try:
    headers = {'user-agent': 'my user agent 1.0',
              'from': 'youremail@domain.com'}

    r = requests.get(url, headers = headers)

except:
    print('Connection error. Kan server niet vinden.')
    sys.exit()

if r.status_code // 100 == 2:
    soup = bs4.BeautifulSoup(r.text, "html.parser")

    print('Links:')
    for e in soup.find_all('a'):
        href = e.get('href')
        if href and href.startswith('http'):
            print(href)

    print('Images')
    for e in soup.find_all('img'):
        src = e.get('src')
        if src and src.startswith('http'):
            print(src)
