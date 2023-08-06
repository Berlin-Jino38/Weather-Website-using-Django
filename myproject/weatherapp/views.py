import datetime
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
import requests
from .form import MyCustomForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

def index(request):
    if request.user.is_authenticated:
        if 'city' in request.POST:
            city = request.POST["city"]
        else:
            city = "Paloor"  # Corrected the city name
            
        appid = '890fd942dceaf606e3ad587a7d227169'
        URL = 'https://api.openweathermap.org/data/2.5/weather'
        PARAMS = {'q': city, 'appid': appid, 'units': 'metric'}
        r = requests.get(url=URL, params=PARAMS)
            
        if r.status_code == 200:
            try:
                res = r.json()
                description = res['weather'][0]['description']
                icon = res['weather'][0]['icon']
                temp = res['main']['temp']

                day = datetime.date.today()
                template = loader.get_template("weatherapp/index.html")
                context = {'description': description, 'icon': icon, 'temp': temp, 'day': day, 'city': city}
                return HttpResponse(template.render(context, request))
            except KeyError:
                error_message = "Error: Unexpected response format from the API"
        else:
            error_message = f"Error: API request failed with status code {r.status_code}"

        return HttpResponse(error_message)
    else:
        messages.error(request, "User must login to see temperature")
        return redirect('/')
 
def login_page(request):
    if request.user.is_authenticated:
         return redirect('/')
    else:
        if request.method == 'POST':
            name = request.POST.get('username')
            pwd = request.POST.get('Password')
            user = authenticate(request, username=name, password=pwd)
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in successfully")
                return redirect('/home/')
            else:
                messages.error(request, "Invalid User Name or Password")
        template=loader.get_template('weatherapp/login.html')
        return HttpResponse(template.render({},request))

def register(request):
    form= MyCustomForm()
    if request.method=='POST':
        form=MyCustomForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Sucess you can login Now..!")
            return redirect('login')
    template=loader.get_template('weatherapp/register.html')
    return HttpResponse(template.render({'form':form},request))
def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged out sucessfully")
    return redirect('/')

def user_page(request):
    if request.user.is_authenticated:
        user = request.user
        template=loader.get_template('weatherapp/user.html')
        return HttpResponse(template.render({'user':user},request))
        