
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse

from .models import Players

menu = [{'title': 'Biz haqimizda', 'url_name': 'about'},
        {'title': 'Post qo`shish', 'url_name': 'add_page'},
        {'title': 'Bog`lanish', 'url_name': 'contact'},
        {'title': 'Chiqish', 'url_name': 'login'},
]

def index(request):
    posts = Players.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Asosiy sahifa'
    }
    return render(request, 'players/index.html', context=context)

def about(request):
    return render(request, 'players/about.html', {'menu': menu, 'title': 'Biz haqimizda'})
    
def addpage(request): 
    return HttpResponse("Post qo`shish")

def contact(request): 
    return HttpResponse("Bog`lanish")

def login(request): 
    return HttpResponse("Avtorizatsiya")

def pageNotFound(request, exception):
    return HttpResponse('<h1>Afsus sahifa topilmadi. </h1>')

def show_post(request, post_id):
    return HttpResponse(f"Id: {post_id}")

