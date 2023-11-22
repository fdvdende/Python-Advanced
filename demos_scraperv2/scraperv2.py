import requests
from bs4 import BeautifulSoup

def scrape_links(url):
    # Check if the URL has a scheme, if not, prepend 'http://'
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'http://' + url

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract all links on the page
        links = soup.find_all('a')

        # Print the extracted links
        for link in links:
            print(link.get('href'))

    else:
        print(f"Error: Unable to fetch the web page. Status code: {response.status_code}")

def scrape_images(url):
    # Check if the URL has a scheme, if not, prepend 'http://'
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'http://' + url

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract all image sources on the page
        images = soup.find_all('img')

        # Print the extracted image sources
        for img in images:
            print(img.get('src'))

    else:
        print(f"Error: Unable to fetch the web page. Status code: {response.status_code}")

# Prompt the user to input a URL
url_to_scrape = input("Enter the URL you want to scrape: ")

# Prompt the user to choose the type of content to scrape
choice = input("Choose the type of content to scrape (1: Links, 2: Images): ")

if choice == '1':
    scrape_links(url_to_scrape)
elif choice == '2':
    scrape_images(url_to_scrape)
else:
    print("Invalid choice. Please choose a valid option.")
