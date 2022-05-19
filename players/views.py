
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse

from .models import Players

menu = ["Biz haqimizda", "Post qo`shish", "Bog`lanish", "Chiqish"]

def index(request):
    posts = Players.objects.all()
    return render(request, 'players/index.html', {'posts': posts,'menu': menu, 'title': 'Asosiy sahifa'})

def about(request):
    return render(request, 'players/about.html', {'menu': menu, 'title': 'Biz haqimizda'})
    
def categories(request, catid): 
    return HttpResponse(f"<h1>Kategoriyalar</h1><p>{catid}</p>")

def archive(request, year): 
    if int(year)>2022: 
        return redirect('home', permanent=False)

    return HttpResponse(f"<h1>Arxiv yillar</h1><p>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponse('<h1>Afsus sahifa topilmadi. </h1>')

