from django.shortcuts import render
from lab_1.views import mhs_name, birth_date

#TODO Implement
#Create a content paragraph for your landing page:
landing_page_content = "Hello there. The name is Benny William Pardede from University of Indonesia. Please stay tuned at my journey to reach Computer Science Degree. Apparently I failed miserably in every WDP labs and quizzes."

def index(request):
    response = {'name': mhs_name, 'content': landing_page_content}
    return render(request, 'index_lab2.html', response)
