from django.urls import path
from . import views

# app_name='polls'
urlpatterns = [
    path('', views.toLogin_view),  # 与views里面的相应
    path('index/', views.Login_view),
    path('toregister/', views.toregister_view),
    path('register/', views.register_view),
    path('publish/', views.publish_view),
    path('update_publish/', views.update_publish_view),
    path('update/', views.update_view),
    path("publish/<int:page>", views.publish_view, name="publish"),
    path('finishdorm/', views.finishdorm_view),
    path('showdist/', views.showdist_view),
    path('showdist_go/', views.showdist_go_view),
    path('showdist_update/', views.update_showdist_view),
    path('add_punish_go/', views.add_punish_go_view),
    path('add_punish/', views.add_punish_view),
    path('add_reward_go/', views.add_reward_go_view),
    path('add_reward/', views.add_reward_view),
    path('ad_search_major/', views.ad_search_major_view),
    path('apply_reward/', views.apply_reward_view),
    path('update_apply/', views.update_apply_view),
    path('ad_search_dist/', views.ad_search_dist_view),
    path('search_student/', views.search_student_view),
    path('show_information/', views.show_information_view),
    path('adstate/', views.adstate_view),
    # path('ad_amountstate/', views.ad_amountstate_view),
    path('adsearch_punish/', views.adsearch_punish_view),
    path('adsearch_p/', views.adsearch_p_view),
    path('adsearch_amount_index/', views.adsearch_amount_index_view),
    path('ad_one_amountstate/', views.ad_one_amountstate_view),
    path('ad_all_amount/', views.ad_all_amount_view),
    path('finishdist/', views.finishdist_view),
    path('upload_file_go/', views.upload_file_go_view),
    path('upload_file/', views.upload_file_view),
    path('adshow_admin/',views.adshow_admin_view),
    # path('admin_danger/', views.admin_danger_view)
]
