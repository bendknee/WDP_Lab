from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Friend
from .api_csui_helper.csui_helper import CSUIhelper
import os
import json

response = {}
csui_helper = CSUIhelper()


def index(request):
    # Page halaman menampilkan list mahasiswa yang ada
    # TODO berikan akses token dari backend dengan menggunakaan helper yang ada

    all_mahasiswa = csui_helper.instance.get_mahasiswa_list()

    friend_list = Friend.objects.all()
    auth = csui_helper.instance.get_auth_param_dict()
    page = request.GET.get('page', 1)
    paginate_data = paginate_page(page, all_mahasiswa)
    mahasiswa = paginate_data['data']
    page_range = paginate_data['page_range']

    response = {"mahasiswa_list": mahasiswa, "friend_list": friend_list, "page_range": page_range, "auth": auth}
    html = 'lab_7/lab_7.html'
    return render(request, html, response)


def paginate_page(page, data_list):
    paginator = Paginator(data_list, 10)

    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    # Get the index of the current page
    index = data.number - 1
    # This value is maximum index of your pages, so the last page - 1
    max_index = len(paginator.page_range)
    # You want a range of 10, so lets calculate where to slice the list
    start_index = index if index >= 10 else 0
    end_index = 10 if index < max_index - 10 else max_index
    # Get our new page range. In the latest versions of Django page_range returns
    # an iterator. Thus pass it to list, to make our slice possible again.
    page_range = list(paginator.page_range)[start_index:end_index]
    paginate_data = {'data': data, 'page_range': page_range}
    return paginate_data


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
        taken = Friend.objects.filter(npm__iexact=npm).exists()
        if not taken:
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
