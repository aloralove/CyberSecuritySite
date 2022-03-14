from django.http import HttpResponse, response
from django.shortcuts import render

def index(request):
    return response(request, 'base.html', {})
    
def home(response):
    return render(response, "CatWebsiteApplication/homepage.html", {})

