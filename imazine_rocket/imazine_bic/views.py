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

def signup(request):
    if request.method == "POST":
        if request.POST["pwd"] == request.POST["rePwd"]:
            user = User.objects.create_user(
                username = request.POST["username"], password = request.POST["pwd"]) 
            auth.login(request, user)
            return redirect('home')
        return render(request, 'imazine_bic/signup.html')
    return render(request, 'imazine_bic/signup.html')

# def login(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = auth.authenticate(request, username=username, password=password)
#         if user is not None:
#             auth.login(request, user)
#             return redirect('home')
#         else:
#             return render(request, 'login.html', {'error': 'username or password is incorrect'})
#     else:
#         return render(request, 'login.html')

# def logout(request):
#     auth.logout(request)
#     return redirect('home')