from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index_user', views.index_user, name='index_user'),
    path('index_company',views.index_company, name='index_company'),
]