from django.shortcuts import render
from .models import User, Company
from django.http import JsonResponse


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
    companys = Company.objects.filter(company_loc = 'oogaki')
    count = 0
    return render(request, 'imazine_bic/reservation_2.html', {'companys':companys,'count':count})

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

def checkEmail(request):
    try:
        user = User.objects.get(id=request.GET['email'])
    except Exception as e:
        user = None
    result = {
        'result':'success',
        # 'data' : model_to_dict(user)  # console에서 확인
        'data' : "not exist" if user is None else "exist"
    }
    return JsonResponse(result)

# def checkEmail(request):
#     print("check email!!!")
#     if request.method == "GET":
#         id = request.GET["email"]
#         users = User.objects.filter(id = id)
#         print(len(users))
#         if len(users) > 0:
#             return JsonResponse({ "success": "false" })
#         else:
#             return JsonResponse({ "success": "true" })

#     return JsonResponse({})

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