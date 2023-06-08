# all_views.py
# Import necessary functions to run our web app
from pyramid.response import Response
from pyramid.view import view_config

# view_config functions tells Pyramid which route's view is going to be defined in the function that follows
# the name of the function does not matter, you can name it whatever you like

@view_config(route_name='intro')
def home_page(request):
    header = '<h2 style="text-align: center;">Home Page</h2>'
    body = '<br><br><p style="text-align: center; font-family: verdana; color: blue;">Hi, My name is Junaid Khalid.</p>'
    body += '<p style="text-align: center; font-family: verdana;"> This is my portfolio website.</p>'
    footer = '<p style="text-align: center; font-family: verdana;">Checkout my <a href="/jobs">previous jobs</a>.</p>'

    # In the 'a' tag, notice that the href contains '/jobs', this route will be defined in the intro.py file
    # It is simply telling the view to navigate to that route, and run whatever code is in that view

    return Response(header + body + footer)

@view_config(route_name='jobs')
def job_history(request):
    header = '<h2 style="text-align: center;">Job History</h2>'
    job1 = '<p style="text-align: center; font-family: verdana;">Jr. Software Developer at XYZ</p>'

    return Response(header + job1)