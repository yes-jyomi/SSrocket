from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index_user', views.index_user, name='index_user'),
    path('index_company',views.index_company, name='index_company'),
    path('reservation_1',views.reservation_1, name='reservation_1'),
    path('reservation_2',views.reservation_2, name='reservation_2'),
    path('reservation_3',views.reservation_3, name='reservation_3'),
    path('reservation_4',views.reservation_4, name='reservation_4'),
    path('signup',views.signup, name='signup'),
    path('../',views.index, name="history"),
]