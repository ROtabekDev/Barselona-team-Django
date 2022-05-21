
from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404, HttpResponse

from .forms import AddPostForm

from .models import Players, Category

menu = [{'title': 'Biz haqimizda', 'url_name': 'about'},
        {'title': 'Futbolchi qo`shish', 'url_name': 'add_page'},
        {'title': 'Bog`lanish', 'url_name': 'contact'},
        {'title': 'Chiqish', 'url_name': 'login'},
]

def index(request):
    posts = Players.objects.all() 

    context = {
        'posts': posts, 
        'menu': menu,
        'title': 'Asosiy sahifa',
        'cat_selected': 0,
    }

    return render(request, 'players/index.html', context=context)

def about(request):
    return render(request, 'players/about.html', {'menu': menu, 'title': 'Biz haqimizda'})
    
def addpage(request): 
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            #print(form.cleaned_data)
            try:
                Players.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, 'Error')
    else:
        form = AddPostForm()
    return render(request, 'players/addpage.html', {'form': form,'menu': menu, 'title': 'Futbolchi qo`shish'})

def contact(request): 
    return HttpResponse("Bog`lanish")

def login(request): 
    return HttpResponse("Avtorizatsiya")

def pageNotFound(request, exception):
    return HttpResponse('<h1>Afsus sahifa topilmadi. </h1>')

def show_post(request, post_slug):
    post = get_object_or_404(Players, pk=post_slug)

    context = {
        'post': post, 
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'players/post.html', context=context) 

def show_category(request, cat_id):
    posts = Players.objects.filter(cat_id=cat_id) 

    context = {
        'posts': posts, 
        'menu': menu,
        'title': 'Kategoriya',
        'cat_selected': cat_id,
    }

    return render(request, 'players/index.html', context=context) 

