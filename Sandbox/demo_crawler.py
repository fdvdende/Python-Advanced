import requests
from bs4 import BeautifulSoup

import logging
import re
from urllib.parse import urljoin

logging.basicConfig(level = logging.ERROR)

hrefs = set()
been_there = set()
emails = set()

def crawl(url):
    hrefs.discard(url)
    been_there.add(url)

    if not url.startswith('http'):
        url = 'https://' + url

    try:
        response = requests.get(url)

    except Exception as ex:
        logging.warning(f'{url} => {ex}')
        return

    if response.status_code == 200:
        logging.info(f'Inspecting {url}')

        html = response.text
        try:
            soup = BeautifulSoup(html, 'html.parser')
        except Exception:
            logging.warning(f'{url} => Error parsing')

        links = soup('a')
        for link in links:
            if 'href' in dict(link.attrs):
                href = link['href']
                # logging.info(f'href {href}')
                if href.startswith('/'):
                    href = urljoin(url, href)
                if href.startswith('#') or href.startswith('javascript'):
                    continue
                if href in been_there:
                    continue
                hrefs.add(href)

        matcher = re.compile(r'\w+@\w+\.\w{2,4}')
        matches = matcher.findall(soup.text)
        if matches:
            for email in matches:
                if email not in emails:
                    print(f'Email: {email}')
            emails.update(matches)

    else:
        logging.warning(f'{url} => {response.status_code}')



url = input('URL of starting point for this crawler: ')

try:
    crawl(url)
    while hrefs:
        url = hrefs.pop()
        crawl(url)
        print(f'Found {len(hrefs)} links and {len(emails)} e-mail addresses.')

except KeyboardInterrupt:
    print('Stopped by user.')

print(f'Found {len(emails)} e-mail addresses:')
for email in emails:
    print(f'{email}')

