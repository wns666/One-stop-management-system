from django.urls import path
from . import views

# app_name='polls'
urlpatterns = [
    path('', views.toLogin_view),  # 与views里面的相应
    path('index/', views.Login_view),
    path('toregister/', views.toregister_view),
    path('register/', views.register_view),
    path('showrp_list/', views.showrp_list_view),
    path('showtotal_list/', views.showtotal_list_view),
    path('showinfor/', views.showinfor_view),
    path('upam/', views.upam_view),
    path('finupam/', views.finupam_view),
    path('showrecord/', views.showrecord_view),
    path('showinformation/', views.showinformation_view),
    path('show_updateinform/', views.show_updateinform_view),
    path('finupdateinformation/', views.finupdateinformation_view),
    path('applyreward/', views.applyreward_view),
    path('add_reward/', views.add_reward_view)
]
