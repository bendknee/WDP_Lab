from django.shortcuts import render
from lab_1.views import mhs_name, birth_date

#TODO Implement
#Create a content paragraph for your landing page:
landing_page_content = "Hi there it's me Benny. Feel free to look around my page. While you're here, don't forgot to follow all my social media accounts. Thank you. "

def index(request):
    response = {'name': mhs_name, 'content': landing_page_content}
    return render(request, 'index_lab2.html', response)
