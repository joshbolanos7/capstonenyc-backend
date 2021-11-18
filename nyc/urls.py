from django.urls import path
from . import views 
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('landmarks/', views.LandmarkList.as_view(), name='landmark_list'),
    path('landmarks/<int:pk>', views.LandmarkDetail.as_view(), name='landmark_detail'),
]






# urlpatterns = [
#     path('', views.landmark_list, name='landmark_list'),
#     path('landmarks/', views.landmark_list, name='landmark_list'),
#     path('landmarks/<int:pk>', views.landmark_detail, name='landmark_detail'),
#     path('landmark/new', views.landmark_create, name='landmark_create'),
#     path('landmark/<int:pk>/edit', views.landmark_edit, name='landmark_edit'),
#     path('landmark/<int:pk>/delete', views.landmark_delete, name='landmark_delete'),
# ]   