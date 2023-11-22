import os
import requests
import sys

import bs4


url = input('Geef URL: ')

if not url.startswith('http'):
    url = 'http://' + url

print(f'OK. Going to scrap "{url}".')

try:
    r = requests.get(url)

except requests.exceptions.ConnectionError as ex:
    print(f'Cannot find url "{url}"')
    sys.exit()

if r.status_code in range(200, 299):
    print('Found and loaded site')

else:
    print(f'Error loading site. Status code: {r.status_code}')
    sys.exit()


soup = bs4.BeautifulSoup(r.content, features="html.parser")

images = soup.find_all('img')

for img in images:
    img_url = img.get('src')
    if not url.endswith('/'):
        url += '/'
    if not img_url.startswith('http'):
        img_url = url + img_url
    print(img_url)

yesno = input('Do you want to download these images? [Y/N]: ')
if yesno.upper().startswith('Y'):

    destination = 'images'
    if not os.path.exists(destination):
        os.mkdir(destination)

    for img in images:
        img_url = img.get('src')
        if not url.endswith('/'):
            url += '/'
        if not img_url.startswith('http'):
            img_url = url + img_url

        img_data = requests.get(img_url).content

        filename = os.path.basename(img_url)
        with open(os.path.join(destination, filename), 'wb') as handler:
            handler.write(img_data)
