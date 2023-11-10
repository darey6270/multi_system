from django.urls import path
from . import views

app_name = 'multi_levelsystem'

urlpatterns = [
    path('', views.HomeView.as_view(), name="index"),
    path('about/', views.AboutView.as_view(), name="about"),
    path('contact/', views.ContactView.as_view(), name="contact"),
    # path('user_register/', views.UserRegister.as_view(), name="user_register"),
]
