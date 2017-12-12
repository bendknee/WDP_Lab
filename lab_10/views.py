# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from .omdb_api import get_detail_movie, search_movie
from .utils import *

response = {}


# Create your views here.

### USER
def index(request):
    # print ("#==> masuk index")
    if 'user_login' in request.session:
        return HttpResponseRedirect(reverse('lab-10:dashboard'))
    else:
        response['author'] = get_data_user(request, 'user_login')
        html = 'lab_10/login.html'
        return render(request, html, response)


def dashboard(request):
    print("#==> dashboard")

    if not 'user_login' in request.session.keys():
        return HttpResponseRedirect(reverse('lab-10:index'))
    else:
        set_data_for_session(request)
        kode_identitas = get_data_user(request, 'kode_identitas')
        try:
            pengguna = Pengguna.objects.get(kode_identitas=kode_identitas)
        except Exception as e:
            pengguna = create_new_user(request)

        movies_id = get_my_movies_from_session(request)
        save_movies_to_database(pengguna, movies_id)

        html = 'lab_10/dashboard.html'
        return render(request, html, response)


### MOVIE : LIST and DETAIL
def movie_list(request):
    judul, tahun = get_parameter_request(request)
    urlDataTables = "/lab-10/api/movie/" + judul + "/" + tahun
    jsonUrlDT = json.dumps(urlDataTables)
    response['jsonUrlDT'] = jsonUrlDT
    response['judul'] = judul
    response['tahun'] = tahun

    get_data_session(request)

    html = 'lab_10/movie/list.html'
    return render(request, html, response)


def movie_detail(request, id):
    print("MOVIE DETAIL = ", id)
    response['id'] = id
    if get_data_user(request, 'user_login'):
        is_added = check_movie_in_database(request, id)
    else:
        is_added = check_movie_in_session(request, id)

    response['added'] = is_added
    response['movie'] = get_detail_movie(id)
    html = 'lab_10/movie/detail.html'
    return render(request, html, response)


### WATCH LATER : ADD and LIST
def add_watch_later(request, id):
    print("ADD WL => ", id)
    msg = "Berhasil tambah movie ke Watch Later"
    if get_data_user(request, 'user_login'):
        print("TO DB")
        is_in_db = check_movie_in_database(request, id)
        if not is_in_db:
            add_item_to_database(request, id)
        else:
            msg = "Movie already exist on DATABASE! Hacking detected!"
    else:
        print("TO SESSION")
        is_in_ssn = check_movie_in_session(request, id)
        if not is_in_ssn:
            add_item_to_session(request, id)
        else:
            msg = "Movie already exist on SESSION! Hacking detected!"

    messages.success(request, msg)
    return HttpResponseRedirect(reverse('lab-10:movie_detail', args=(id,)))


def list_watch_later(request):
    #  Implement this function by yourself
    get_data_session(request)
    moviesku = []
    if get_data_user(request, 'user_login'):
        moviesku = get_my_movies_from_database(request)
    else:
        moviesku = get_my_movies_from_session(request)

    watch_later_movies = get_list_movie_from_api(moviesku)

    response['watch_later_movies'] = watch_later_movies
    html = 'lab_10/movie/watch_later.html'
    return render(request, html, response)


### SESSION : GET and SET
def get_data_session(request):
    if get_data_user(request, 'user_login'):
        response['author'] = get_data_user(request, 'user_login')


def set_data_for_session(request):
    response['author'] = get_data_user(request, 'user_login')
    response['kode_identitas'] = request.session['kode_identitas']
    response['role'] = request.session['role']


### API : SEARCH movie
def api_search_movie(request, judul, tahun):
    print("API SEARCH MOVIE")
    if judul == "-" and tahun == "-":
        items = []
    else:
        search_results = search_movie(judul, tahun)
        items = search_results

    dataJson = json.dumps({"dataku": items})
    mimetype = 'application/json'
    return HttpResponse(dataJson, mimetype)
