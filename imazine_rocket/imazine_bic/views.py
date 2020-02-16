from django.shortcuts import render
from .models import User, Company
from django.http import JsonResponse


# Create your views here.
def index(request):
    users = User.objects.filter(id = 'test1')
    return render(request, 'imazine_bic/main.html', {'users':users})

def choose_lan(request):
    return render(request, 'imazine_bic/choose_lan.html')

def choose_loc(request):
    users = User.objects.filter(id = 'test1')
    return render(request, 'imazine_bic/choose_loc.html', {'users':users})

def choose_shop(request):
    # company_loc = request.
    companys = Company.objects.filter(company_loc = 'oogaki')
    count = 0
    return render(request, 'imazine_bic/choose_shop.html', {'companys':companys,'count':count})

def choose_time(request):
    return render(request, 'imazine_bic/choose_time.html')

def choose_end(request):
    return render(request, 'imazine_bic/choose_end.html')

def signup(request):
    if request.method == "POST":
        if request.POST["pwd"] == request.POST["rePwd"]:
            user = User.objects.create_user(
                username = request.POST["username"], password = request.POST["pwd"]) 
            auth.login(request, user)
            return redirect('home')
        return render(request, 'imazine_bic/signup.html')
    return render(request, 'imazine_bic/signup.html')

def checkEmail(request):
    print("check email!!!")
    if request.method == "GET":
        id = request.GET["email"]
        users = User.objects.filter(id = id)
        print(len(users))
        if len(users) > 0:
            return JsonResponse({ "success": "false" })
        else:
            return JsonResponse({ "success": "true" })

    return JsonResponse({})

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