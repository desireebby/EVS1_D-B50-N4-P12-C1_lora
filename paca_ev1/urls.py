"""paca_ev1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from paca_app1 import views as paca_app1
from paca_app2 import views as paca_app2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola/', paca_app1.display),
    path('ahora/', paca_app1.displayDateTime),
    path('hola2/', paca_app2.display),
    path('ahora2/', paca_app2.displayDateTime),
    
]
