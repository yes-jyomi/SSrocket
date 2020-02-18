from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import HttpResponse, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.utils.translation import ugettext_lazy as _
from django.utils import translation


def translate(request, lan):
    if lan == 'ko' or lan == 'en' or lan == 'jp':
        if translation.LANGUAGE_SESSION_KEY in request.session:
            del(request.session[translation.LANGUAGE_SESSION_KEY])
        translation.activate(lan)
        request.session[translation.LANGUAGE_SESSION_KEY] = f'{lan}'
    else:
        if translation.LANGUAGE_SESSION_KEY in request.session:
            del(request.session[translation.LANGUAGE_SESSION_KEY])
        translation.activate('en')
        request.session[translation.LANGUAGE_SESSION_KEY] = 'ko'

# Create your views here.
def index(request):
    lan = request.COOKIES.get('lan')
    translate(request, lan)

    id = request.COOKIES.get('id') 
    users = User.objects.filter(id = id)
    response = render(request, 'imazine_bic/main.html', {'users':users})
    response.set_cookie('id',id)
    return response

@csrf_exempt
def choose_lan(request):
    if request.method == "POST":
        lan = request.POST['lan']
        translate(request, lan)
        
        id = request.COOKIES.get('id') 
        count = 1
        response = render(request, 'imazine_bic/signin.html',{"count":count})
        response.set_cookie('id',id)
        response.set_cookie('lan',lan)
        return response
    return render(request, 'imazine_bic/choose_lan.html')

@csrf_exempt
def choose_loc(request):
    id = request.COOKIES.get('id') 
    users = User.objects.filter(id = id)
    if request.method == "POST":
        count = 1
        response = render(request, 'imazine_bic/choose_shop.html',{"count":count})
        response.set_cookie('company_loc',request.POST['company_loc'])
        response.set_cookie('id',id)
        return response
    return render(request, 'imazine_bic/choose_loc.html',{"users":users})

@csrf_exempt#,{"count":count}
def choose_shop(request):
    company_loc = request.COOKIES.get('company_loc') 
    companys = Company.objects.filter(company_loc = company_loc)
    if request.method == "POST":
        id = request.COOKIES.get('id') 
        response = render(request, 'imazine_bic/choise_time.html',{"companys":companys})
    return render(request, 'imazine_bic/choose_shop.html',{"companys":companys})

@csrf_exempt#,{"count":count}
def choose_time(request):
    print(request.COOKIES)
    id = request.COOKIES.get('id') 
    company_loc=request.COOKIES.get('company_loc')
    company_num=request.COOKIES.get('company_num')
    companys = Company.objects.filter(company_num = company_num)
    print(company_num)
    if request.method == "POST":
        r_year = request.POST['r_year']
        r_month = request.POST['r_month']
        r_date = request.POST['r_date']
        r_b = request.POST['r_btime']
        r_r = request.POST['r_rtime']
        r_btime = "{}-{}-{} {}".format(r_year,r_month,r_date,r_b)#datetime formatting
        r_rtime = "{}-{}-{} {}".format(r_year,r_month,r_date,r_r)
        #db insert
        history = History.objects.create(company_num=company_num, member_id = id, r_btime = r_btime, r_rtime = r_rtime, reserved_At = datetime.datetime.now())
        response = render(request, 'imazine_bic/reservation_check.html',{"history":history})
        companys = Company.objects.filter(company_num=company_num)
        for company in companys:
            Company.objects.update(rent_num=company.rent_num+1)
        return response
    return render(request, 'imazine_bic/choose_time.html',{"companys":companys})

def choose_end(request):
    return render(request, 'imazine_bic/choose_end.html')

@csrf_exempt
def signup(request):
    if request.method == "POST":
        lan = request.COOKIES.get('lan')
        translate(request, lan)

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
        lan = request.COOKIES.get('lan')
        translate(request, lan)

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

@csrf_exempt
def shop_detail(request, pk):
    shop = get_object_or_404(Company, pk=pk)
    id = request.COOKIES.get('id') 
    users = User.objects.filter(id = id)
    response = render(request, 'imazine_bic/choose_time.html', {'shop': shop})
    response.set_cookie('company_num',pk)
    if request.method == "GET":
        return response
    return render(request, 'imazine_bic/shop_detail.html', {'shop': shop,'count':1, 'users':users})

def notice_detail(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    return render(request, 'imazine_bic/notice_detail.html', {'notice': notice})

@csrf_exempt
def setting(request):
    if request.method == "POST":
        return render(request, 'imazine_bic/setting/'+request.setUrl+".html")
    return render(request, 'imazine_bic/setting.html')

def setUrl(request, setUrl):
    if setUrl == "" :
        ren = render(request, 'imazine_bic/setting.html')
    elif setUrl == "modify":
        ren = render(request, 'imazine_bic/setting_modify.html')
    elif setUrl == "secession":
        ren = render(request, 'imazine_bic/setting_secession.html')
    elif setUrl == "counsel":
        ren = render(request, 'imazine_bic/setting_counsel.html')
    return ren

def counsel(request):
    id = request.COOKIES.get('id')
    counsels = Counsel.objects.filter(v = id)
    if request.method == "POST":
        category = request.POST['category']
        response = render(request, 'imazine_bic/setting_write.html')
        response.set_cookie("category",category)
        return response
    return request(request, 'imazine_bic/setting_counsel.html',{"counsels":counsels,"count":1})

def write(request):
    if request.method == "POST":
        category = request.COOKIES.get('category')
        id = request.COOKIES.get('id')
        subject = request.POST['subject']
        content = request.POST['content']
        counsel = Counsel.objects.create(member_id = id, subject = subject, content = content, regdate = datetime.datetime.now(), category = category)
        response = render(request, 'imazine_bic/setting_write.html',{"count":2})
        return response
    return request(request, 'imazine_bic/setting_write.html',{"count":1})