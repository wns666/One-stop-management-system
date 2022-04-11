from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.utils import timezone
from random import sample

from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


#
def toLogin_view(request):
    return render(request, 'login.html')


def toregister_view(request):
    return render(request, 'register.html')


def register_view(request):
    u = request.POST.get("w_no", '')
    n = request.POST.get("w_name", '')
    p = request.POST.get("w_pass", '')
    c = WInit.objects.filter(w_no=u, w_name=n).count()
    if u and n and p and c:
        x = WDist.objects.get(w_no=u)
        zc = WStup(w_ano=x.w_ano, w_pass=p, w_no=u)
        zc.save()
        return HttpResponseRedirect("/polls")
    else:
        return render(request, 'register.html')


def Login_view(request):
    u = request.POST.get("w_ano", '')
    p = request.POST.get("w_pass", '')
    if u and p:
        c = WStup.objects.filter(w_ano=u, w_pass=p).count()
        d = WStup.objects.filter(w_no=u, w_pass=p).count()
        if c >= 1:
            show_stu = WDist.objects.get(w_ano=u)
            show_stu2 = WMajor.objects.get(w_mno=show_stu.w_mno)
            request.session["login_user"] = u
            return render(request, "index.html", locals())  # 给个响应
        elif d >= 1:
            show_stu = WDist.objects.get(w_no=u)
            show_stu2 = WMajor.objects.get(w_mno=show_stu.w_mno)
            request.session["login_user"] = show_stu.w_ano
            return render(request, "index.html", locals())  # 给个响应
        else:
            error_msg = '用户名或密码错误'
            return render(request, 'login.html', {'error_msg': error_msg})


def showrp_list_view(request):
    x = request.session["login_user"]
    reward_list = WReward.objects.filter(w_ano=x)  # 这里不用get的原因是get只能返回一个
    punish_list = WPunish.objects.filter(w_ano=x)
    return render(request, "showrp_list.html", locals())


def showtotal_list_view(request):
    x = request.session["login_user"]
    total_list = WTotal.objects.get(w_ano=x)
    y = total_list.w_amount1 - total_list.w_amount2
    return render(request, "showtotal_list.html", locals())


def upam_view(request):
    x = request.session["login_user"]
    return render(request, "upam.html", locals())


def finupam_view(request):
    u = request.POST.get("am", '')
    x = request.session["login_user"]
    v = WTotal.objects.get(w_ano=x)
    z = int(u)
    WTotal.objects.filter(w_ano=x).update(w_amount2=z + v.w_amount2)
    total_list = WTotal.objects.get(w_ano=x)
    y = total_list.w_amount1 - total_list.w_amount2
    # 填入到缴费的记录表里面
    c = WDist.objects.get(w_ano=x)
    d = timezone.now().date()
    e = str(d)
    e = e.replace('-', '')
    zc = WRecord(w_ano=x, w_name=c.w_name, w_date=e, w_amount=z)
    zc.save()
    return render(request, "showtotal_list.html", locals())
