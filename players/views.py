
from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import AddPostForm
from .models import Players, Category
from .utils import menu, DataMixin
from django.core.paginator import Paginator



class PlayersHome(DataMixin, ListView): 
    model = Players
    template_name = 'players/index.html'
    context_object_name = 'posts' 

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs) 
        c_def = self.get_user_context(title='Asosiy sahifa')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Players.objects.filter(is_published=True)


# def index(request):
#     posts = Players.objects.all() 

#     context = {
#         'posts': posts, 
#         'menu': menu,
#         'title': 'Asosiy sahifa',
#         'cat_selected': 0,
#     }
#     return render(request, 'players/index.html', context=context)

def about(request):
    contect_list = Players.objects.all()
    paginator = Paginator(contect_list, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'players/about.html', {'menu': menu, 'title': 'Biz haqimizda'})
    

class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name: str = 'players/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs) 
        c_def = self.get_user_context(title= 'Futbolchi qo`shish')
        return dict(list(context.items()) + list(c_def.items()))

# def addpage(request): 
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             #print(form.cleaned_data)
#             form.save()
#             return redirect('home') 
#     else:
#         form = AddPostForm()
#     return render(request, 'players/addpage.html', {'form': form,'menu': menu, 'title': 'Futbolchi qo`shish'})

def contact(request): 
    return HttpResponse("Bog`lanish")

def login(request): 
    return HttpResponse("Avtorizatsiya")

def pageNotFound(request, exception):
    return HttpResponse('<h1>Afsus sahifa topilmadi. </h1>')


class ShowPost(DataMixin, DetailView):
    model = Players
    template_name: str = 'players/post.html'
    slug_url_kwarg: str = 'post_slug'
    context_object_name = 'post'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs) 
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


# def show_post(request, post_slug):
#     post = get_object_or_404(Players, slug=post_slug)

#     context = {
#         'post': post, 
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }

#     return render(request, 'players/post.html', context=context) 

class PlayersCategory(DataMixin, ListView): 
    model = Players
    template_name = 'players/index.html'
    context_object_name = 'posts'
    allow_empty: bool = False

    def get_queryset(self):
        return Players.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['cat_selected'] = context['posts'][0].cat_id
        c_def = self.get_user_context(title='Kategoriya - ' + str(context['posts'][0].cat), cat_selected = context['posts'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))

# def show_category(request, cat_id):
#     posts = Players.objects.filter(cat_id=cat_id) 

#     if len(posts) == 0:
#         raise Http404

#     context = {
#         'posts': posts, 
#         'menu': menu,
#         'title': 'Kategoriya',
#         'cat_selected': cat_id,
#     }

#     return render(request, 'players/index.html', context=context) 

