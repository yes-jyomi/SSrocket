from django.shortcuts import render
from .models import User, Company

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
    # company_loc = request.
    companys = Company.objects.filter(company_loc = 'oogaki')
    count = 0
    return render(request, 'imazine_bic/reservation_2.html', {'companys':companys,'count':count})

def reservation_3(request):
    return render(request, 'imazine_bic/reservation_3.html')

def reservation_4(request):
    return render(request, 'imazine_bic/reservation_4.html')

def signup(request):
    return render(request, 'imazine_bic/signup.html')
