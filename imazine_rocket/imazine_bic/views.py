from django.shortcuts import render
from .models import User, Company
from django.http import JsonResponse
from django.contrib.auth.models import User


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
        if request.POST["pw"] == request.POST["repw"]:
            user = User.objects.create(
                username = request.POST["s_name"], email = request.POST["email"], password = request.POST["pw"]) 
            # auth.login(request, user)
            return render(request, 'imazine_bic/signin.html')
        return render(request, 'imazine_bic/signup.html')
    return render(request, 'imazine_bic/signup.html')
 
def signin(request):
    if request.method == "POST":
        print("post")
        id = request.POST['id']
        pwd = request.POST['pwd']
        users = User.objects.get(id = id)
        if users is not None:
            for user in users:
                if id == user.id and pwd == user.pwd:
                    print("okay")
                return render(request, 'imazine_bic/main.html')
        else:
            print("noo")
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    else:
        print("signin으로")
        return render(request, 'imazine_bic/signin.html')

def checkEmail(request):
    try:
        user = User.objects.get(email=request.GET['email'])
    except Exception as e:
        user = None
    result = {
        'result':'success',
        # 'data' : model_to_dict(user)  # console에서 확인
        'data' : "not exist" if user is None else "exist"
    }
    return JsonResponse(result)
