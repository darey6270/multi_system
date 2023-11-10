from django.urls import path
from . import views

app_name = 'activities'
urlpatterns = [
    path('log_info_list/', views.LogInfoListView.as_view(), name='log_info_list'),
    path('log_report/', views.LogReportListView.as_view(), name='log_report'),
    # path('user_log_info_list/', views.UserLogInfoListView.as_view(), name='user_log_info_list'),
    # path('create/', views.LogInfoCreateView.as_view(), name='log_info_create'),
    #path('<int:pk>/update/', views.LogInfoUpdateView.as_view(), name='log_info_update'),
    path('<int:pk>/', views.LogInfoDetailView.as_view(), name='log_info_detail'),
    # path('detail/<int:pk>/', views.UserLogInfoDetailView.as_view(), name='user_log_info_detail'),
    path('<int:pk>/delete/', views.LogInfoDeleteView.as_view(), name='log_info_delete'),
    path('<int:pk>/<int:log>/update_status/', views.updateStatus, name="update_status")
]
