from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'imazine_bic/main.html', {})
def index_user(request):
    return render(request, 'imazine_bic/index_user.html', {})

def index_company(request):
    return render(request, 'imazine_bic/index_company.html', {})

