from django.shortcuts import render
from .models import *
from django.http import HttpResponse, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt,csrf_protect 


# Create your views here.
def index(request):
    print("index")
    id = request.COOKIES.get('id') 
    print(id,"엥")
    users = User.objects.filter(id = id)
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

@csrf_exempt
def signup(request):
    if request.method == "POST":
        id = request.POST['email']
        name = request.POST['name']
        pwd = request.POST['pw']
        info = int(request.POST['info'])
        user = User.objects.create(id = id, name = name, pwd = pwd, info = info)
        return render(request, 'imazine_bic/signin.html')
    return render(request, 'imazine_bic/signup.html')
 
@csrf_exempt
def signin(request):
    if request.method == "POST":
        id = request.POST['id']
        pwd = request.POST['pwd']
        users = User.objects.filter(id = id)
        if users is not None:
            for user in users:
                if id == user.id and pwd == user.pwd:
                    response = render(request, 'imazine_bic/main.html',{"okay":1})
                    response.set_cookie('id',id)
                    print("okay")
                    return response
        return HttpResponse("<html><script>alert('로그인 오류입니다. 다시 시도해주세요');location.href='signin';</script></html>")
    else:
        return render(request, 'imazine_bic/signin.html')

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
