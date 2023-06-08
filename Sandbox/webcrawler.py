import requests
import bs4

been_there = set()

def get_links(url):
    try:
        r = requests.get(url)
    except:
        return

    soup = bs4.BeautifulSoup(r.text, "html.parser")

    links = []
    for anchor in soup.find_all('a'):
        link = anchor.get('href', '/')
        if link.startswith('/'):
            link = 'https://www.defensie.nl' + link
        if link not in been_there:
            been_there.add(link)
            links.append(link)
    return links

url = 'https://www.defensie.nl'

links = get_links(url)

with open('been_there.txt', 'w') as f:

    for link in links:
        print(link)
        f.write(link + '\n')
        links2 = get_links(link)
        if links2 is None:
            continue
        else:
            for link2 in links2:
                print('>', link2)
                f.write(link2 + '\n')

                links3 = get_links(link2)
                if links3 is None:
                    continue
                else:
                    for link3 in links3:
                        print('>>', link3)
                        f.write(link3 + '\n')

                        links3 = get_links(link3)

