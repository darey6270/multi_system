from django.urls import path
from . import views

app_name='app_user'

urlpatterns = [
    # path('',views.HomeView.as_view(),name="index"),
    # path('dashboard/',views.DashboardView.as_view(),name="dashboard"),
    path('register/', views.register, name="register"),
    path('user_login/', views.login, name="user_login"),
    path('user_logout/', views.user_logout, name="user_logout"),

]
