from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def first(request):
    return render(request, 'first_list.html')


def info_movies(request, slug_movies):
    if slug_movies in ['duna_2']:
        return render(request, 'info_duna2.html')
    if slug_movies in ['pchelovod']:
        return render(request, 'info_pchelovod.html')
    return HttpResponseNotFound('<img src=https://mir-s3-cdn-cf.behance.net/project_modules/1400/aa545434520589.56d6d1275928c.jpg></img>')

