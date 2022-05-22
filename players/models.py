
from django.db import models
from django.urls import reverse

class Players(models.Model):
    title = models.CharField(max_length=255, verbose_name='FISH')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name='Biografiya')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Rasm')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')
    time_update = models.DateTimeField(auto_now=True, verbose_name='O`zgartirilgan vaqti')
    is_published = models.BooleanField(default=True, verbose_name='Chop etilgan')
    cat = models.ForeignKey("Category", on_delete=models.PROTECT,verbose_name='Kategoriya')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Futbolchi'
        verbose_name_plural = 'Futbolchilar'

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Pozitsiya'
        verbose_name_plural = 'Pozitsiyalar'
