from django.urls import path
from bugs import views

urlpatterns = [
    path('trends/', views.bug_trends, name='bug_trends'),
]
