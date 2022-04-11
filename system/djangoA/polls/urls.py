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
    path('upam/', views.upam_view),
    path('finupam/', views.finupam_view)
]
