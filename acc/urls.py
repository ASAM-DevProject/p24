from django.urls import path

from acc.views import Profile

app_name = 'account'

urlpatterns = [
    path('account/profile/', Profile.as_view(), name='profile')
]