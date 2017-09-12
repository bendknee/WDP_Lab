from django.shortcuts import render
from lab_1.views import mhs_name, birth_date
#Create a list of biodata that you wanna show on webpage:
#[{'subject' : 'Name', 'value' : 'Igor'},{{'subject' : 'Birth Date', 'value' : '11 August 1970'},{{'subject' : 'Sex', 'value' : 'Male'}
#TODO Implement
bio_dict = [{'subject' : 'Name', 'value' : mhs_name},\
{'subject' : 'Birth Date', 'value' : birth_date.strftime('%d %B %Y')},\
{'subject' : 'Sex', 'value' : 'Male'}]

def index(request):
    response = {"bio_dict":bio_dict}
    return render(request, 'description_lab2addon.html', response)

# Create your views here.
