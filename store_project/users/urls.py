from django.urls import path
from . import views

urlpatterns = [
    path('', views.sign_in, name='sign-in'),
    path('sign-out/', views.sign_out, name='sign-out'),
]