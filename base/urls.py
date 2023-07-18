from django.urls import path
from . import views

urlpatterns= [
    path('', views.home, name = 'home'),
    path('blog/', views.blog, name = 'blog'),
    path('contact/', views.contact, name = 'contact'),
    path('shoppingcart/', views.shoppingcart, name = 'shoppingcart'),
    path('dashboard/', views.dashboard, name = 'dashborad'),
    path('login/', views.login, name = 'login'),
]