from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

from .models import Friend
from .api_csui_helper.csui_helper import CSUIhelper
import os
import json

response = {}
csui_helper = CSUIhelper()


def index(request):
    # Page halaman menampilkan list mahasiswa yang ada
    # TODO berikan akses token dari backend dengan menggunakaan helper yang ada

    mahasiswa_list = csui_helper.instance.get_mahasiswa_list()

    friend_list = Friend.objects.all()
    auth = csui_helper.instance.get_auth_param_dict()
    response = {"mahasiswa_list": mahasiswa_list, "friend_list": friend_list, "auth": auth}
    html = 'lab_7/lab_7.html'
    return render(request, html, response)


def friend_list(request):
    friend_list = Friend.objects.all()
    response['friend_list'] = friend_list
    html = 'lab_7/daftar_teman.html'
    return render(request, html, response)


def get_friend_list(request):
    if request.method == 'GET':
        friend_list = Friend.objects.all()
        data = serializers.serialize('json', friend_list)
        return HttpResponse(data)


@csrf_exempt
def add_friend(request):
    if request.method == 'POST':
        name = request.POST['name']
        npm = request.POST['npm']
        friend = Friend(friend_name=name, npm=npm)
        friend.save()
        data = model_to_dict(friend)
        return HttpResponse(data)


def delete_friend(request, friend_id):
    Friend.objects.filter(id=friend_id).delete()
    return HttpResponseRedirect('/lab-7/friend-list')


@csrf_exempt
def validate_npm(request):
    npm = request.POST.get('npm', None)
    data = {
        # lakukan pengecekan apakah Friend dgn npm tsb sudah ada
        'is_taken': Friend.objects.filter(npm__iexact=npm).exists()
    }
    return JsonResponse(data)


def model_to_dict(obj):
    data = serializers.serialize('json', [obj, ])
    struct = json.loads(data)
    data = json.dumps(struct[0]["fields"])
    return data
