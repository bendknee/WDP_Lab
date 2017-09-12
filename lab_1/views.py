from django.shortcuts import render
from datetime import datetime, date
# Enter your name here
mhs_name = 'Benny William Pardede' # TODO Implement this
curr_year = int(datetime.now().strftime("%Y"))
birth_date = date(1997, 11, 10) #TODO Implement this, format (Year, Month, Date)
# Create your views here.
def index(request):
    response = {'name': mhs_name, 'age': calculate_age(birth_date.year)}
    return render(request, 'index_lab1.html', response)

def calculate_age(birth_year):
    return curr_year - birth_year if birth_year <= curr_year else 0
