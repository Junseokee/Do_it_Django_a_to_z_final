from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.about_me),
    path('', views.landing),

]
