from django.urls import path,include
from . import views
import requests



city="Manama"
urlpatterns = [
  path('', views.home, name='home'),
 
  path('display/f', views.forecaste, name='forecaste'),
  path('display/', views.display, name='display'),
  path('display/', views.RecordCrt.as_view(), name='create'),


  
  path('about/', views.about, name='about'),
  path('test/', views.test, name='aboutshotter'),
  path('accounts/signup', views.signup, name='signup'),
  path('accounts/', include('django.contrib.auth.urls')),
#   path('records/', views.records_index, name='index'),
]