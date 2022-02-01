from django.shortcuts import redirect, render
from django.views.generic import CreateView, ListView
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required

from acc.models import User, ProfileSick, ProfileDoctor
from acc.forms import SickSignUpForms, DoctorSignUpForms

# Create your views here.

def login_doctor(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None and user.is_doctor==True:
            login(request, user)
            return redirect('acc:profile')
        else:
            return redirect('login_doctor')
    else:
        return redirect('login_doctor')

def login_sick(requset):
    if requset.method == 'POST':
        username = requset.POST['username']
        password = requset.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None and user.is_sick==True:
            login(requset, user)
            return redirect('acc:profile')
        else:
            return redirect('login_sick')
    else:
        return redirect('login_sick')

@login_required
def logout(requset):
    django_logout(requset)
    return redirect('home:home')

class RegisterSick(CreateView):
    model = User
    form_class = SickSignUpForms
    template_name = 'registeration/register_sick.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()

        return redirect('/')

class RegisterDoctor(CreateView):
    model = User
    form_class = DoctorSignUpForms
    template_name = 'registeration/register_doctor.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()

        return redirect('/')

class Profile(ListView):
    template_name = 'registeration/profile.html'
    context_object_name = 'object'

    def get_queryset(self):
        if self.request.user.is_sick == True:
            return ProfileSick.objects.get(user__id=self.request.user.id)
        if self.request.user.is_doctor == True:
            return ProfileDoctor.objects.get(user__id=self.request.user.id)