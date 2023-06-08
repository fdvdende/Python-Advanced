# intro.py
# from https://stackabuse.com/introduction-to-the-python-pyramid-framework/
# Import necessary functions to run our web app

from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

# This function receives a request from the user, and returns a response
def intro(request):
    return Response('<h2 style="text-align: center; font-family: verdana; color: blue;">Pyramid Mini Web Framework</h2>')


# This function will start a server on our computer (localhost), define the
# routes for our application, and also add a view to be shown to the user
def main():
    with Configurator() as config:

        config.add_route('intro', '/')
        config.add_view(intro, route_name='intro')
        application = config.make_wsgi_app()

    # 8000 is the port number through which the requests of our app will be served
    server = make_server('0.0.0.0', 8000, application)
    server.serve_forever()

main()