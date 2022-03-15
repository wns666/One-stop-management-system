from django.urls import path
from . import views

# app_name='polls'
urlpatterns = [
    path('', views.toLogin_view),  # 与views里面的相应
    path('index/', views.Login_view),
    path('toregister/', views.toregister_view),
    path('register/', views.register_view),
]
