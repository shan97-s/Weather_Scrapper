from django.shortcuts import render,redirect
# importing the library
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
#user section
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Forecasting Records Sections

from django.views.generic.edit import CreateView, UpdateView, DeleteView
#Inserting data into database
from django import forms
from django.forms import modelform_factory
from django.http import HttpResponse
import pymysql
from weather_app.models import Records
from django.forms import Textarea
# RecordForm=modelform_factory(Records,fields=('city','temp'))
# Form.modelform_factory(Records,form=RecordForm,widgets={'city':}
# Form.values.append()
import uuid
import boto3
# Add the following import
from django.http import HttpResponse




def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('display')
    else:
      error_message = 'Invalid credentials - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)










# Define the home view
def about(request):
  return render(request, 'about.html')

def home(request):
  return render(request, 'home.html')

def base(request):
  return render(request, 'base.html')

def test(request):
    url = 'https://www.msn.com/en-us/weather/maps?in-Vladivostok/animation=0&type=radar'
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')
    divf = soup.find('div', attrs={'id': 'root'}).text
    return HttpResponse(f'<h1>Welcome to dashboard</h1>{divf}')

#   driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
#   url='https://www.google.com/search?q=+weather+Manama'
#   driver.get(url)
#   html=driver.page_source
#   soup=BeautifulSoup(html, 'html.parser')
array=[]
returns=array
city=''
def forecaste(request):
   city=request.POST.get('city')
   n = request.POST.get('city')
   url=f'https://www.google.com/search?hl=en&q=+weather+{city}'
   html=requests.get(url).content
   soup=BeautifulSoup(html, 'html.parser')
   temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
   star = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
   listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
   strd = listdiv[5].text
   pos = strd.find('Wind')
   other_data = strd[pos:]
   data = star.split('\n')
   time = data[0]
   sky = data[1]
   res= f'<h1>Results are {temp}, {sky},<br/> {time} </h1>'
   context={'list':[{'c':city,'temp':temp,'sky':sky,'t':time}]}
   array.append(context)
   returns=array
#    return render(request,'about.html',{
#      'temperature':returns
#    })
   return redirect('create')


class RecordCrt(LoginRequiredMixin, CreateView):
    model = Records
    fields = ['city','temp']
    

    def form_valid(self, form):
       # Assign the logged in user
       form.instance.user = self.request.user
    #    form.instance.fields.city="ok_status"
    #    # Let the CreateView do its job as usual
    # #    RecordForm=modelform_factory(Records,fields=('city'))
    # #    form=modelform_factory(Records,form=RecordForm,widgets={'city':Textarea})
    #    city = form.CharField(
    #    label='Name', 
    #    widget=forms.TextInput(attrs={'placeholder': 'Type name here...'})
    #     )
    #    class Meta:
    #     model = Records
    #     fields = ('city', 'temp')
    #     widgets = {
    #         'city': forms.CharField(attrs={'placeholder': "Search Content..."})
    #     }
       return super().form_valid(form)
    def send(request):
      p = Records(city='Berkeley', temp='20')
      p.save()
    #    return redirect('display')

RecordForm=modelform_factory(Records,fields=('city','temp'))
Form=modelform_factory(Records,form=RecordForm,widgets={'city':city})
# sent=Form.values()
name=""   
def display(request):
  
  name = request.POST.get('city')
    

   
  
#   output= run([sys.executable, '//Users//will/Documents//GitHub//FBZbot//env//FBZ//ShopBot//app.py',name],shell=False,stdout=PIPE)
  
  return render(request, 'about.html',{
    'temperature':returns,
    'n':name
    # 'check':sent
   })
# def records_index(request):
#     forecasted_records = Cat.objects.all()
#     return render(request, 'records/index.html', {
#         'records': forecasted_records 
#     })

