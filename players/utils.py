
 
from players.models import Category
from django.db.models import Count

menu = [{'title': 'Biz haqimizda', 'url_name': 'about'},
        {'title': 'Futbolchi qo`shish', 'url_name': 'add_page'},
        {'title': 'Bog`lanish', 'url_name': 'contact'},
        {'title': 'Chiqish', 'url_name': 'login'},
]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('players'))
        
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)
        
        context['menu'] = user_menu
        context['cats'] = cats

        if 'cat_selected' not in context:
            context['can_selected'] = 0
        return context