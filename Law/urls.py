from django.urls import path
from .import views




urlpatterns = [
    path('', views.law_home_view, name='law-home'),
    path('law-contact/', views.law_contact_view, name='law-contact'),
    path('law-field/', views.law_field_view, name='law-field'),
    path('law-our-team/', views.law_team_view, name='law-our-team'),
    path('law-about-us/', views.law_about_us_view, name='law-about-us')
]
