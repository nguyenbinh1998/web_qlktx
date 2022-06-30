"""project_datn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ktx.hust/', include('web_ql_ktx.urls'))
]


# /admin
#/admin/user 
#/admin/user GET : respone json(list user)
#/admin/user POST : respone json(new user)
#/admin/user/:user-id : layas user theo id respone json (user Id)

#/admin
#/admin/rooom
#/admin/room GET : respone json(list room)
#/admin/room POST : respone json(new room)
#/admin/room/:room-id : layas room theo id respone json (room Id)
