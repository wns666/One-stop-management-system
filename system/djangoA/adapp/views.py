from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from random import sample
from django.db.models import F, Q
from django.shortcuts import render

from polls.models import *
from django.http import HttpResponseRedirect
import xlrd
# from django.db import connection
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
            v = WAdmin.objects.get(w_adno=u)
            request.session["login_user"] = u
            request.session["login_type"] = v.w_type
            request.session.set_expiry(0)
            admin_user = request.session["login_user"]
            admin_type = request.session["login_type"]
            return render(request, "adindex.html", locals())  # 给个响应
        else:
            error_msg = '用户名或密码错误'
            return render(request, 'adlogin.html', {'error_msg': error_msg})


def ad_search_major_view(request):
    admin_user = request.session["login_user"]
    admin_type = request.session["login_type"]
    publisher_obj_list1 = WMajor.objects.all()
    return render(request, "admajor_list.html", locals())


def publish_view(request):
    # 显示宿舍的列表
    admin_user = request.session["login_user"]
    admin_type = request.session["login_type"]
    u = request.POST.get("mno", '')
    publisher_obj_list1 = WMajor.objects.filter(w_mno=u)  # 获取所有数据
    return render(request, "admajor_list.html", locals())


def update_publish_view(request):
    # 转到修改界面
    admin_user = request.session["login_user"]
    admin_type = request.session["login_type"]
    u = request.GET.get("id")  # 这个id传来的是需要修改的那一行的id
    return render(request, "admajor_update.html", locals())


def update_view(request):
    # 把已经修改的寝室数据写入数据库
    admin_user = request.session["login_user"]
    admin_type = request.session["login_type"]
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
    admin_user = request.session["login_user"]
    admin_type = request.session["login_type"]
    showdist_obj_list = WDist.objects.all()
    return render(request, "addist_list.html", locals())


def showdist_view(request):
    admin_user = request.session["login_user"]
    admin_type = request.session["login_type"]
    u = request.POST.get("mno", '')
    showdist_obj_list = WDist.objects.filter(w_mno=u)
    return render(request, "addist_list.html", locals())


def showdist_go_view(request):
    admin_user = request.session["login_user"]
    admin_type = request.session["login_type"]
    u = request.GET.get("id")
    v = WInit.objects.get(w_no=u)
    w = v.w_mno
    return render(request, "addist_update.html", locals())


def update_showdist_view(request):
    admin_user = request.session["login_user"]
    admin_type = request.session["login_type"]
    u = request.POST.get("id", '')
    w = request.POST.get("mno", '')
    p = request.POST.get("class", '')
    v = request.POST.get("ano", '')
    x = request.POST.get("dno", '')
    # return render(request,"check.html",locals())
    WDist.objects.filter(w_no=u).update(w_class=p, w_ano=v, w_dno=x)  # 修改数据库里面的数据
    showdist_obj_list = WDist.objects.filter(w_mno=w)
    return render(request, "addist_list.html", locals())


def finishdist_view(request):
    WTotal.objects.all().delete()
    WInform.objects.all().delete()
    max_mno = 4
    for i in range(1, max_mno + 1):
        s = "A"
        stu_mno = str(i)
        mno_len = len(stu_mno)
        for j in range(3 - mno_len):
            stu_mno = "0" + stu_mno
        s += stu_mno
        s += "18"
        stu_mno = "0" + stu_mno
        stu_list = WDist.objects.filter(w_mno=stu_mno).order_by('w_no')
        # return render(request, "check.html", locals())
        num = 0
        for j in stu_list:
            stu_class = str(j.w_class)
            s1 = s + str(stu_class[-1])
            num += 1
            len1 = len(str(num))
            for k in range(3 - len1):
                s1 += "0"
            s1 += str(num)
            WDist.objects.filter(w_no=j.w_no).update(w_ano=s1)
            fee_l = WMajor.objects.get(w_mno=stu_mno)
            zc = WTotal(w_ano=s1, w_name=j.w_name, w_state="未报到", w_amount2="0", w_amount1=fee_l.w_fee)
            zc.save()
            zd = WInform(w_ano=s1)
            zd.save()
    return HttpResponseRedirect("/adapp/ad_search_dist/")


def add_punish_go_view(request):
    admin_user = request.session["login_user"]
    admin_type = request.session["login_type"]
    return render(request, "adadd_punish.html", locals())


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
    admin_user = request.session["login_user"]
    admin_type = request.session["login_type"]
    return render(request, "adadd_reward.html", locals())


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
    return HttpResponseRedirect("/adapp/add_reward_go/")


def apply_reward_view(request):
    admin_user = request.session["login_user"]
    admin_type = request.session["login_type"]
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
    admin_user = request.session["login_user"]
    admin_type = request.session["login_type"]
    return render(request, "adsearch.html", locals())


def show_information_view(request):
    admin_user = request.session["login_user"]
    admin_type = request.session["login_type"]
    u = request.POST.get("id", '')
    num = WDist.objects.count()
    if num >= 1:
        ad_stu2 = WDist.objects.get(w_ano=u)
        ad_stu3 = WInform.objects.get(w_ano=u)
        ad_stu4 = WTotal.objects.get(w_ano=u)
        reward_list = WReward.objects.filter(w_ano=u)
        return render(request, "adinformation.html", locals())
    else:
        error_msg = '学号输入错误'
        return render(request, "adsearch.html", {'error_msg': error_msg})


def adstate_view(request):
    admin_user = request.session["login_user"]
    admin_type = request.session["login_type"]
    v = request.POST.get("state", '')
    u = request.POST.get("ano", '')
    # if v == "退学":
    #     WDist.objects.filter(w_ano=u).delete()
    WTotal.objects.filter(w_ano=u).update(w_state=v)
    ad_stu2 = WDist.objects.get(w_ano=u)
    ad_stu3 = WInform.objects.get(w_ano=u)
    ad_stu4 = WTotal.objects.get(w_ano=u)
    return render(request, "adinformation.html", locals())


# def ad_amountstate_view(request):
#     # amount_list = WTotal.objects.filter(w_amount2__lt=F('w_amount2'))
#     amount_list = WTotal.objects.filter(w_amount2__lt=F('w_amount1'))
#     return render(request, "adamountstate.html", locals())


def adsearch_punish_view(request):
    admin_user = request.session["login_user"]
    admin_type = request.session["login_type"]
    punish_list = WPunish.objects.all().order_by('-w_date')
    return render(request, "ad_punish.html", locals())


def adsearch_p_view(request):
    admin_user = request.session["login_user"]
    admin_type = request.session["login_type"]
    u = request.POST.get("id", '')
    punish_list = WPunish.objects.filter(Q(w_date=u) | Q(w_ano=u) | Q(w_name=u) | Q(w_pl=u) | Q(w_thing__contains=u))
    return render(request, "ad_punish.html", locals())


def adsearch_amount_index_view(request):
    admin_user = request.session["login_user"]
    admin_type = request.session["login_type"]
    return render(request, "adsearch_amount_index.html", locals())


def ad_one_amountstate_view(request):
    admin_user = request.session["login_user"]
    admin_type = request.session["login_type"]
    u = request.POST.get("id", '')
    v = WTotal.objects.get(w_ano=u)
    amount_list = WRecord.objects.filter(w_ano=u)
    return render(request, "ad_stuamount.html", locals())


def ad_all_amount_view(request):
    admin_user = request.session["login_user"]
    admin_type = request.session["login_type"]
    u = request.POST.get("state", '')
    v = request.POST.get("id", '')
    if u == "1":
        amount_list = WRecord.objects.filter(w_date=v)
        return render(request, "ad_all_amount_list.html", locals())
    else:
        if u == "0":
            amount_list = WTotal.objects.filter(w_amount2__lt=F('w_amount1'), w_state="在读")
            amount_list2 = WTotal.objects.filter(w_amount2__gte=F('w_amount1'), w_state="在读")
        elif u == "mno":
            amount_list = WTotal.objects.raw(
                'select w_abs.w_total.* from w_total,w_dist where w_total.w_ano = w_dist.w_ano and w_dist.w_mno = %s and w_total.w_amount1>w_total.w_amount2 and w_total.w_state="在读"',
                [v])
            amount_list2 = WTotal.objects.raw(
                'select w_abs.w_total.* from w_total,w_dist where w_total.w_ano = w_dist.w_ano and w_dist.w_mno = %s and w_total.w_amount1<=w_total.w_amount2 and w_total.w_state="在读"',
                [v])
        elif u == "class":
            amount_list = WTotal.objects.raw(
                'select w_abs.w_total.* from w_total,w_dist where w_total.w_ano = w_dist.w_ano and w_dist.w_class = %s and w_total.w_amount1>w_total.w_amount2 and w_total.w_state="在读"',
                [v])
            amount_list2 = WTotal.objects.raw(
                'select w_abs.w_total.* from w_total,w_dist where w_total.w_ano = w_dist.w_ano and w_dist.w_class = %s and w_total.w_amount1<=w_total.w_amount2 and w_total.w_state="在读"',
                [v])
        # 查找学号在dist表里专业号为v
        return render(request, "ad_all_amount.html", locals())


def upload_file_go_view(request):
    admin_user = request.session["login_user"]
    admin_type = request.session["login_type"]
    return render(request, "adupload_file.html", locals())


def upload_file_view(request):
    f = request.FILES.get('file')
    u = request.POST.get("state", '')
    # return render(request, "check.html", locals())
    excel_type = f.name.split('.')[1]
    if excel_type in ['xlsx', 'xls']:
        wb = xlrd.open_workbook(filename=None, file_contents=f.read())
        table = wb.sheets()[0]
        rows = table.nrows  # 总行数
        # 从第二行开始存，因为第一行是题头
        for i in range(1, rows):
            rowVlaues = table.row_values(i)
            if u == "0":
                zc = WInit(w_no=rowVlaues[0], w_lno=rowVlaues[1], w_name=rowVlaues[2], w_sex=rowVlaues[3],
                           w_mno=rowVlaues[4], w_school=rowVlaues[5])
                zc.save()
                zd = WDist(w_no=rowVlaues[0], w_name=rowVlaues[2], w_sex=rowVlaues[3],
                           w_mno=rowVlaues[4])
                zd.save()
            else:
                zc = WMajor(w_mno=rowVlaues[0], w_mname=rowVlaues[1], w_fee=rowVlaues[2])
                zc.save()
        return HttpResponseRedirect("/adapp/ad_search_dist/")
    else:
        return HttpResponse("格式错误")


def adshow_admin_view(request):
    admin_user = request.session["login_user"]
    admin_type = request.session["login_type"]
    admin_list = WAdmin.objects.filter(w_type__range=(1, 3))

    return render(request, "adshow_admin.html", locals())


def update_admin_view(request):
    u = request.POST.get("w_type", '')
    v = request.POST.get("w_adno", '')
    w = request.POST.get("w_pass", '')
    if u == "1":
        WAdmin.objects.filter(w_adno=v).update(w_type=u, w_typeinform="学生管理工作人员")
    if u == "2":
        WAdmin.objects.filter(w_adno=v).update(w_type=u, w_typeinform="专业管理工作人员")
    if u == "3":
        WAdmin.objects.filter(w_adno=v).update(w_type=u, w_typeinform="财务管理工作人员")
    if w:
        WAdmin.objects.filter(w_adno=v).update(w_pass=w)
    return HttpResponseRedirect("/adapp/adshow_admin")


def detel_admin_view(request):
    u = request.GET.get("id")
    WAdmin.objects.filter(w_adno=u).delete()
    return HttpResponseRedirect("/adapp/adshow_admin")


def adadd_admin_view(request):
    u = request.POST.get("w_newadmin", '')
    zc = WAdmin(w_adno=u, w_pass="12138", w_type="1", w_typeinform="学生管理工作人员")
    zc.save()
    return HttpResponseRedirect("/adapp/adshow_admin")
