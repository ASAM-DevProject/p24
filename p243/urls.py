"""p24 URL Configuration

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
from django.conf.urls.static import static
from django.conf import settings

from acc.views import login_doctor, login_sick, logout, RegisterSick, RegisterDoctor

urlpatterns = [
    path('admin/', admin.site.urls),
    path('visiit/', include('visit.urls')),
    path('', include('acc.urls')),
    path('', include('home.urls')),
    
    path('login/sick/', login_sick, name='login_sick'),
    path('login/doctor/', login_doctor, name='login_doctor'),
    path('logout/', logout, name='logout'),

    path('register/sick/', RegisterSick.as_view(), name='register_sick'),
    path('register/doctor/', RegisterDoctor.as_view(), name='register_doctor'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
