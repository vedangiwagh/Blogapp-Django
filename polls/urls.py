from django.urls import path
from . import views

urlpatterns  = [
    path('', views.home, name='home'),
    path('add_post', views.add_post, name='add_post'),
    path('view_post/<int:no>', views.view_post, name='view_post'),
    path('list_post', views.list_post, name='list_post'),
]
