"""
URL configuration for petMarket project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from pets.views import index
from my_app.views import page1, page2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pets/', index),
    # path('pets/', include('pets.urls')) # path('pets/', include('pets.urls')) # Второй способ описан в pets.urls
    path('page1/', page1),
    path('page2/', page2),
]



