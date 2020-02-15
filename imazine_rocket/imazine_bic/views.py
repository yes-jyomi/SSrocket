from django.shortcuts import render
from .models import User

# Create your views here.
def index(request):
    users = User.objects.filter(id = 'test1')
    return render(request, 'imazine_bic/main.html', {'users':users})
def index_user(request):
    return render(request, 'imazine_bic/index_user.html', {})

def index_company(request):
    return render(request, 'imazine_bic/index_company.html', {})

def reservation_1(request):
    users = User.objects.filter(id = 'test1')
    return render(request, 'imazine_bic/reservation_1.html', {'users':users})

def reservation_2(request):
    return render(request, 'imazine_bic/reservation_2.html')

def reservation_3(request):
    return render(request, 'imazine_bic/reservation_3.html')

def reservation_4(request):
    return render(request, 'imazine_bic/reservation_4.html')