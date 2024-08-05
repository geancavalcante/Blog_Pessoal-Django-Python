
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('postagens/', views.publish, name='postagens'),
    path('sobre/', views.sobre, name='sobre'),
    path('livros/', views.books, name='livros'),
    path('formulário/', views.authentication, name='formulário'),
    path('formulário/blog', views.form_posting, name='formulário_postagens'),
    path('formulário/livros', views.form_book, name='formulário_livros'),
]