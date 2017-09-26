from django.shortcuts import render
from lab_2.views import landing_page_content
from django.http import HttpResponseRedirect
from .forms import Message_Form
from .models import Message


# Create your views here.
response = {'author': "Benny William Pardede"} #TODO Implement yourname
about_me = ["I am now 19 yo. Soon to be 20", "A year ago I got the chance to be a computer science student", "I do not code everyday", "I had sleeping problems", "Sometimes I think that I am actually Squidward", "If Lightning McQueen bought an insurance, is it a life insurance or a car insurance", "I need to tell everyone every 2 minutes that I am a certified doorknob", "Mike Myers"]

def index(request):
    response['content'] = landing_page_content
    html = 'lab_4/lab_4.html'
    #TODO Implement, isilah dengan 6 kata yang mendeskripsikan anda
    response['about_me'] = about_me
    response['message_form'] = Message_Form
    return render(request, html, response)


def message_post(request):
    form = Message_Form(request.POST or None)
    if(request.method == 'POST' and form.is_valid()):
        response['name'] = request.POST['name'] if request.POST['name'] != "" else "Anonymous"
        response['email'] = request.POST['email'] if request.POST['email'] != "" else "Anonymous"
        response['message'] = request.POST['message']
        message = Message(name=response['name'], email=response['email'],
                          message=response['message'])
        message.save()
        html ='lab_4/form_result.html'
        return render(request, html, response)
    else:
        return HttpResponseRedirect('/lab-4/')

def message_table(request):
        message = Message.objects.all()
        response['message'] = message
        html = 'lab_4/table.html'
        return render(request, html , response)

