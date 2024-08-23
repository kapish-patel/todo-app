from django.urls import path

from . import views

urlpatterns = [
    path('', views.IdentityApi.as_view(), name='identity'),
    path('login/', views.IdentityApi.as_view(), name='login'),
]