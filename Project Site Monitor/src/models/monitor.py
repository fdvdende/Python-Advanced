from .site_monitor import SiteMonitor

import json
import os

def monitor():

    dirname = 'data'
    filename = 'sites_to_monitor.json'

    with open(os.path.join(dirname, filename)) as f:
        sites_to_monitor = json.load(f)

    for site in sites_to_monitor:
        site_monitor = SiteMonitor(**site)
        site_monitor.parse()
        site_monitor.update_or_insert()

        print(80 * '-')
        print('Monitoring =>', site['url'])
        print()
        for summary in site_monitor.summary:
            print('>', summary['title'])
            print(' ', summary['link'])
            print(' ', summary['date'])
            print()
