from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from random import sample

from django.shortcuts import render
from .models import *


#
def toLogin_view(request):
    return render(request, '../templates/login.html', {'name': 'wlqtc'})


#
def toregister_view(request):
    return render(request, '../template/register.html')


def toregister_view(request):
    return render(request, 'register.html')


def register_view(request):
    u = request.POST.get("w_no", '')
    n = request.POST.get("w_name", '')
    p = request.POST.get("w_pass", '')
    c = WInit.objects.filter(w_no=u, w_name=n).count()
    if u and n and p and c:
        zc = WStup(w_ano=u, w_pass=p)
        zc.save()
        return HttpResponse("注册成功")
    else:
        return HttpResponse("注册失败")


def Login_view(request):
    u = request.POST.get("w_ano", '')
    p = request.POST.get("w_pass", '')
    if u and p:
        c = WStup.objects.filter(w_ano=u, w_pass=p).count()
        if c >= 1:
            return HttpResponse("登录成功")  # 给个响应
        else:
            return HttpResponse("账号密码错误")  # 给个响应
    else:
        return HttpResponse("账号密码错误")
