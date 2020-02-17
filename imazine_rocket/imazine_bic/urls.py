from django.urls import path
from . import views

urlpatterns = [
    path('',views.choose_lan,name='choose_lan'),
    path('index', views.index, name='index'),
    path('choose_loc',views.choose_loc, name='choose_loc'),
    path('choose_shop',views.choose_shop, name='choose_shop'),
    path('choose_time',views.choose_time, name='choose_time'),
    path('choose_lan',views.choose_lan, name='choose_lan'),
    path('choose_end',views.choose_end, name='choose_end'),
    path('signin',views.signin, name='signin'),
    path('signup',views.signup, name='signup'),
    path('check_email',views.checkEmail, name='check_email'),
    path('choose_use',views.choose_use,name = 'choose_use' ),
]