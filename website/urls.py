from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='home'),
    path('service-details/<str:param>', views.serviceDetails , name='service_details'),
    path('portfolio-details/<str:param>', views.portfolioDetails, name='portfolio_details'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout')
]