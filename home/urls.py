from django.urls import path
from home.views import home, error_access_permission_dr, error_access_permission_sick

app_name = 'home'

urlpatterns = [
    path('', home, name='home'),
    path('permission/sick', error_access_permission_sick, name='permission_sick'),  
    path('permission/dr', error_access_permission_dr, name='permission_dr'),  
]