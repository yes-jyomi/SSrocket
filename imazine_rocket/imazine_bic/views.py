from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import HttpResponse, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt,csrf_protect 


# Create your views here.
def index(request):
    print("index")
    id = request.COOKIES.get('id') 
    print(id,"엥")
    users = User.objects.filter(id = id)
    response = render(request, 'imazine_bic/main.html', {'users':users})
    response.set_cookie('id',id)
    return response

@csrf_exempt
def choose_lan(request):
    if request.method == "POST":
        lan = request.POST['lan']
        print(lan)
        # if lan == "kor":
        #     pass
        #여기에 번역하기 api 사용
        id = request.COOKIES.get('id') 
        count = 1
        response = render(request, 'imazine_bic/choose_loc.html',{"count":count})
        response.set_cookie('id',id)
        return response
    return render(request, 'imazine_bic/choose_lan.html')

@csrf_exempt
def choose_loc(request):
    if request.method == "POST":
        count = 1
        response = render(request, 'imazine_bic/choose_shop.html',{"count":count})
        id = request.COOKIES.get('id') 
        response.set_cookie('company_loc',request.POST['company_loc'])
        response.set_cookie('id',id)
        return response
    return render(request, 'imazine_bic/choose_loc.html')

@csrf_exempt
def choose_shop(request):
    company_loc = request.COOKIES.get('company_loc') 
    companys = Company.objects.filter(company_loc = company_loc)
    if request.method == "POST":
        id = request.COOKIES.get('id') 
        response = render(request, 'imazine_bic/choise_time.html',{"companys":companys})
        response.set_cookie('company_loc',request.POST['company_loc'])
        response.set_cookie('id',id)
        print(company)
        return render(request, 'imazine_bic/choose_time.html')
    return render(request, 'imazine_bic/choose_shop.html',{"companys":companys})

def choose_time(request):
    companys = Company.objects.filter(company_num = 1)
    return render(request, 'imazine_bic/choose_time.html', {'companys':companys})

def choose_end(request):
    return render(request, 'imazine_bic/choose_end.html')

@csrf_exempt
def signup(request):
    if request.method == "POST":
        id = request.POST['id']
        name = request.POST['name']
        pwd = request.POST['pwd']
        info = request.POST['info']
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
        user = User.objects.get(id=request.GET['id'])
    except Exception as e:
        user = None

    result = {
        'result':'success',
        # 'data' : model_to_dict(user)  # console에서 확인
        'data' : "not exist" if user is None else "exist"
    }
    return JsonResponse(result)


def choose_use(request):
    return render(request, 'imazine_bic/choose_use.html')

def notice(request):
    notices = Notice.objects.all().order_by('num')
    for notice in notices:
        print(notice.subject)
    return render(request, 'imazine_bic/notice.html', {'notices':notices})

def shop_detail(request, pk):
    shop = get_object_or_404(Company, pk=pk)
    return render(request, 'imazine_bic/shop_detail.html', {'shop': shop})