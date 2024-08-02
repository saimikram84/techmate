from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='home'),
    path('service-details/<str:param>', views.serviceDetails , name='service_details'),
    path('portfolio-details/<str:param>', views.portfolioDetails, name='portfolio_details')
]