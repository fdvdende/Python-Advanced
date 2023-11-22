from ..persistence.store_in_sqlite import *

import os
from datetime import datetime
import logging
import hashlib
import requests
from bs4 import BeautifulSoup as bs

logging.basicConfig(
    filename = None,  # or to a file 'example.log',
    level = logging.INFO,
    format='%(asctime)s.%(msecs)03d - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%dT%H:%M:%S')


class SiteMonitor:

    def __init__(self,
                 name,
                 url,
                 item_selector,
                 title_selector = None,
                 link_selector = None,
                 date_selector = None,
                 keywords = None):

        self._name = name
        self._url = self.clean_url(url)
        self._item_selector = item_selector
        self._title_selector = title_selector
        self._link_selector = link_selector
        self._date_selector = date_selector
        self._keywords = keywords if keywords else []

        self._soup = None
        self._items = []
        self._summary = []
        self._filename = name.lower().replace(' ', '_') + '.json'

    @property
    def summary(self):
        return self._summary

    @staticmethod
    def clean_url(url):
        if not url.startswith('http'):
            url = 'https://' + url.lower().strip()
        return url

    def get_webpage(self):
        try:
            response = requests.get(self._url)

        except requests.exceptions.ConnectionError:
            logging.warning('Connection Errror on site: ' + self._url)
            return

        if response.status_code not in range(200, 300):  # Not OK
            logging.warning('Status Code Errror on site: ' + self._url)
            return

        else:
            self._soup = bs(response.text, features='html.parser')

    def get_items(self):
        all_items = self._soup.select(self._item_selector)

        # only items with a specified keyword
        if self._keywords:
            self._items = []
            for item in all_items:
                item_text = item.text.lower()
                for keyword in self._keywords:
                    and_keywords = [kw.strip().lower() for kw in keyword.split('AND')]
                    if all(kw in item_text for kw in and_keywords):
                        self._items.append(item)
        else:
            self._items = all_items.copy()


    @staticmethod
    def get_sub_item(item, selector = None):
        selector = selector.strip()
        if selector:
            if ':' not in selector:
                selector += ':'
            css_selector, attribute_name = selector.split(':')
            if css_selector:
                items = item.select(css_selector)
                if items:
                    item = items[0]
            if attribute_name and attribute_name in item.attrs:
                return item.attrs[attribute_name].strip()
            else:
                if item.string:
                    return str(item.string).strip()

    def parse(self):
        self.get_webpage()
        self.get_items()

        self._summary = []
        for item in self._items:

            title = self.get_sub_item(item, self._title_selector)
            link = self.get_sub_item(item, self._link_selector)
            if link and not link.startswith('http'):
                link = os.path.dirname(self._url[:-1]) + link
            date = self.get_sub_item(item, self._date_selector)
            s = f'{self._name} - {title}'
            m = hashlib.sha256()
            m.update(s.encode())
            hash = m.hexdigest()

            self._summary.append(
                {
                    'name': self._name,
                    'url': self._url,
                    'title': title,
                    'link': link,
                    'date': date,
                    'hash': hash,
                    'first_seen': datetime.now().strftime('%Y-%m-%d %H:%M'),
                    'last_seen': datetime.now().strftime('%Y-%m-%d %H:%M'),
                    'status': 'new',     # new, watch, ignore
                    'html': str(item)
                }
            )

    def store(self):
        try:
            previous_summary = load()
            for item in self._summary:
                for old_item in previous_summary:
                    if old_item['title'] == item['title']:
                        item['first_seen'] = old_item['first_seen']
                        item['status'] = old_item['status']
        except:
            pass

        store(self._summary)

    def update_or_insert(self):
        update_or_insert(self._summary)



