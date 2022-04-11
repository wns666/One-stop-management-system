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
    path('add_reward/', views.add_reward_view)
    # path('finishdist/', views.finishdist_view),
]
