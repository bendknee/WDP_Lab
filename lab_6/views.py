from django.shortcuts import render

response = {}
def index(request):
    response['author'] = "Benny William Pardede"
    html = 'lab_6/lab_6.html'
    return render(request, html, response)
