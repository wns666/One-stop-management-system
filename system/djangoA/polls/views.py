from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from random import sample

from django.shortcuts import render
from .models import *


def toLogin_view(request):
    return render(request, '../templates/login.html', {'name': 'wlqtc'})


# def toregister_view(request):
#     return render(request, 'register.html')


# def register_view(request):
#     u = request.POST.get("user", '')
#     p = request.POST.get("pwd", '')
#     if u and p:
#         stu = PollsStudentinfo(stu_name=u, stu_pwd=p)
#         stu.save()
#         return HttpResponse("注册成功")
#     else:
#         return HttpResponse("注册失败")
#
#
# def Login_view(request):
#     u = request.POST.get("user", '')
#     p = request.POST.get("pwd", '')
#     if u and p:
#         c = PollsStudentinfo.objects.filter(stu_name=u, stu_pwd=p).count()
#         if c >= 1:
#             return HttpResponse("登录成功")  # 给个响应
#         else:
#             return HttpResponse("账号密码错误")  # 给个响应
#     else:
#         return HttpResponse("账号密码错误")
