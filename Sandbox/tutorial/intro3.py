# intro.py
# Import necessary functions to run our web app

from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

def main():
    with Configurator() as config:
        # In add_route function, the first parameter defines the name of the route
        # and the second parameter defines the 'route' or the page location
        config.add_route('intro', '/')
        config.add_route('jobs', '/jobs')

        # The scan function scans our project directory for a file named all_views.py
        # and connects the routes we provided above with their relevant views
        config.scan('all_views')

        application = config.make_wsgi_app()

    # The following lines of code configure and start a server which hosts our
    # website locally (i.e. on our computer)
    server = make_server('0.0.0.0', 8000, application)
    server.serve_forever()

main()