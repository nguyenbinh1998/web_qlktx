from django.shortcuts import render

def home(request):
    return render(request, 'web_ql_ktx/home.html')

def login(request):
    return render(request, 'web_ql_ktx/login.html')

def register(request):
    return render(request, 'web_ql_ktx/register.html')