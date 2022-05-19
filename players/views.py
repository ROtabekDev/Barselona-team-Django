import re
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse

def index(request):
    return HttpResponse("Bu yangi app.")

def categories(request, catid): 
    return HttpResponse(f"<h1>Kategoriyalar</h1><p>{catid}</p>")

def archive(request, year): 
    if int(year)>2022: 
        return redirect('home', permanent=False)

    return HttpResponse(f"<h1>Arxiv yillar</h1><p>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponse('<h1>Afsus sahifa topilmadi. </h1>')

