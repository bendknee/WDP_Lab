from django.shortcuts import render

# Create your views here.
response = {}
def index(request):
    response['author'] = "Benny William Pardede"
    html = 'lab_8/lab_8.html'
    return render(request, html, response)
