from django.urls import path
from . import views

urlpatterns = [
    path('', views.bug_list, name='bug_list'),
    path('create/', views.create_bug, name='create_bug'),
    path('<int:pk>/', views.bug_detail, name='bug_detail'),
    path('<int:pk>/update/', views.update_bug, name='update_bug'),
]