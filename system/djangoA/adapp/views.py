from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from random import sample
from django.db.models import F
from django.shortcuts import render

from polls.models import *
from django.http import HttpResponseRedirect
from .models import *


#
def toLogin_view(request):
    return render(request, 'adlogin.html', {'name': 'wlqtc'})


def toregister_view(request):
    return render(request, 'adregister.html')


def register_view(request):
    u = request.POST.get("w_adno", '')
    n = request.POST.get("w_type", '')
    p = request.POST.get("w_pass", '')
    if u and n and p:
        zc = WAdmin(w_adno=u, w_pass=p, w_type=n)
        zc.save()
        return HttpResponseRedirect("/adapp")
    else:
        return render(request, 'adregister.html')


def Login_view(request):
    u = request.POST.get("w_adno", '')
    p = request.POST.get("w_pass", '')
    if u and p:
        c = WAdmin.objects.filter(w_adno=u, w_pass=p).count()
        if c >= 1:
            return render(request, "adindex.html")  # 给个响应
        else:
            error_msg = '用户名或密码错误'
            return render(request, 'adlogin.html', {'error_msg': error_msg})


def ad_search_major_view(request):
    publisher_obj_list1 = WMajor.objects.all()
    return render(request, "admajor_list.html", locals())


def publish_view(request):
    # 显示宿舍的列表
    u = request.POST.get("mno", '')
    publisher_obj_list1 = WMajor.objects.filter(w_mno=u)  # 获取所有数据
    return render(request, "admajor_list.html", locals())


def update_publish_view(request):
    # 转到修改界面
    u = request.GET.get("id")  # 这个id传来的是需要修改的那一行的id
    return render(request, "admajor_update.html",locals())


def update_view(request):
    # 把已经修改的寝室数据写入数据库
    u = request.POST.get("mno", '')
    p = request.POST.get("docu", '')
    v = request.POST.get("docu2", '')
    WMajor.objects.filter(w_mno=u).update(w_dorm=p, w_dorm2=v)  # 修改数据库里面的数据
    publisher_obj_list1 = WMajor.objects.filter(w_mno=u)
    return render(request, "admajor_list.html", locals())


def finishdorm_view(request):
    # 这里是已经完成全部的宿舍分配工作，可以将数据导入到w_dist里面了
    dorm_list = WMajor.objects.all()
    # 循环里面的全部数据
    for dorm2 in dorm_list:
        WDist.objects.filter(w_mno=dorm2.w_mno, w_sex="男").update(w_dorm=dorm2.w_dorm)
        WDist.objects.filter(w_mno=dorm2.w_mno, w_sex="女").update(w_dorm=dorm2.w_dorm2)
    return HttpResponseRedirect("/adapp/ad_search_major")


def ad_search_dist_view(request):
    showdist_obj_list = WDist.objects.all()
    return render(request, "addist_list.html", locals())


def showdist_view(request):
    u = request.POST.get("mno", '')
    showdist_obj_list = WDist.objects.filter(w_mno=u)
    return render(request, "addist_list.html", locals())


def showdist_go_view(request):
    u = request.GET.get("id")
    v = WInit.objects.get(w_no=u)
    w = v.w_mno
    return render(request, "addist_update.html", locals())


def update_showdist_view(request):
    u = request.POST.get("id", '')
    w = request.POST.get("mno", '')
    p = request.POST.get("class", '')
    v = request.POST.get("ano", '')
    x = request.POST.get("dno", '')
    WDist.objects.filter(w_no=u).update(w_class=p, w_ano=v, w_dno=x)  # 修改数据库里面的数据
    showdist_obj_list = WDist.objects.filter(w_mno=w)
    return render(request, "addist_list.html", locals())


# def finishdist_view(request):
#     dist_list = WDist.objects.all()
#     for dist1 in dist_list:
#         WStup.objects.filter(w_ano=dist1.w_no).update(w_ano=dist1.w_ano)
#     return HttpResponseRedirect("/adapp/showdist")


def add_punish_go_view(request):
    return render(request, "adadd_punish.html")


def add_punish_view(request):
    a = request.POST.get("id", '')
    b = request.POST.get("name", '')
    c = request.POST.get("date", '')
    d = request.POST.get("pl", '')
    e = request.POST.get("thing", '')
    zc = WPunish(w_ano=a, w_thing=e, w_date=c, w_name=b, w_pl=d)
    zc.save()
    if d == "退学" or d == "休学":
        WTotal.objects.filter(w_ano=a).update(w_state=d)
    return HttpResponseRedirect("/adapp/add_punish_go/")


def add_reward_go_view(request):
    return render(request, "adadd_reward.html")


def add_reward_view(request):
    a = request.POST.get("id", '')
    b = request.POST.get("name", '')
    c = request.POST.get("date", '')
    d = request.POST.get("thing", '')
    e = request.POST.get("rl", '')
    f = request.POST.get("rname", '')
    g = request.POST.get("organ", '')
    zc = WReward(w_name=b, w_thing=d, w_date=c, w_ano=a, w_rename=f, w_organ=g, w_rl=e)
    zc.save()
    return HttpResponseRedirect("adapp/add_reward_go/")


def apply_reward_view(request):
    aplly_reward_list = WRewardApply.objects.all()
    return render(request, "adapply_reward.html", locals())


def update_apply_view(request):
    u = request.GET.get("id")
    v = u[-1]
    w = u[:-1]
    if v == "1":
        y = WRewardApply.objects.get(w_num=w)
        zc = WReward(w_rename=y.w_rename, w_ano=y.w_ano, w_organ=y.w_organ, w_thing=y.w_thing, w_date=y.w_date,
                     w_name=y.w_name, w_rl=y.w_rl)
        zc.save()
    WRewardApply.objects.filter(w_num=w).delete()
    aplly_reward_list = WRewardApply.objects.all()
    # return render(request, "adapply_reward.html", locals())
    return HttpResponseRedirect("/adapp/apply_reward")


def search_student_view(request):
    return render(request, "adsearch.html")


def show_information_view(request):
    u = request.POST.get("id", '')
    ad_stu2 = WDist.objects.get(w_ano=u)
    ad_stu3 = WInform.objects.get(w_ano=u)
    ad_stu4 = WTotal.objects.get(w_ano=u)
    return render(request, "adinformation.html", locals())


def adstate_view(request):
    v = request.POST.get("state", '')
    u = request.POST.get("ano", '')
    # if v == "退学":
    #     WDist.objects.filter(w_ano=u).delete()
    WTotal.objects.filter(w_ano=u).update(w_state=v)
    ad_stu2 = WDist.objects.get(w_ano=u)
    ad_stu3 = WInform.objects.get(w_ano=u)
    ad_stu4 = WTotal.objects.get(w_ano=u)
    return render(request, "adinformation.html", locals())


def ad_amountstate_view(request):
    # amount_list = WTotal.objects.filter(w_amount2__lt=F('w_amount2'))
    amount_list = WTotal.objects.filter(w_amount2__lt=F('w_amount1'))
    return render(request, "adamountstate.html", locals())