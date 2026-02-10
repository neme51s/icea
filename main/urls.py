from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/company/', views.about_company, name='about_company'),
    path('about/clients/', views.about_clients, name='about_clients'),
    path('about/partners/', views.about_partners, name='about_partners'),
    path('services/valuation/', views.services_valuation, name='services_valuation'),
    path('services/consulting/', views.services_consulting, name='services_consulting'),
    path('services/trainings/', views.services_trainings, name='services_trainings'),
    path('services/legal/', views.services_legal, name='services_legal'),
    path('contacts/', views.contacts, name='contacts'),
    path('download/company-profile/', views.download_company_profile, name='download_company_profile'),
]