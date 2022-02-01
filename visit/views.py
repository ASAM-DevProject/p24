from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required

from visit.forms import CreateVisitTImeForm, PaymentForm
from acc.models import ProfileDoctor, ProfileSick
from visit.models import VisitTime, Specialization
from visit.decorators import doctor_required, sick_required
# Create your views here.



def create_time(time):
    t = time.split(":")
    hour = int(t[0])
    minutes = int(t[1])
    s = int(t[2])
    if minutes <= 60 - 10:
        minutes += 10
        if minutes == 60:
            hour += 1
            minutes = "00"
            time = f'{hour}:{minutes}:{s}'
            return time
        else:
            time = f'{hour}:{minutes}:{s}'
            return time
    else:
        hour += 1
        minutes = 60 - minutes
        time = f'{hour}:0{minutes}:{s}'
        return time
    

@login_required
@doctor_required
def create_visit_table(request):
    context ={}
    # create object of form
    form = CreateVisitTImeForm(request.POST or None, request.FILES or None)
      
    # check if form data is valid
    if form.is_valid():
        count = form.cleaned_data['count']
        date = form.cleaned_data['date']
        time = form.cleaned_data['time']
        
        
        # save the form data to model
        user = ProfileDoctor.objects.get(user=request.user)
        if user.is_doctor == True:
            for i in range(count):
                time = create_time(str(time))
                visit = VisitTime()
                visit.date = date
                visit.time = time
                visit.doctor = user
                visit.count = count
                visit.specialization = user.expertise
                visit.save()
        else:
            return redirect('/')
            
    context['form']= form
    return render(request, "DCVF.html", context)

# @login_required
@sick_required
def specialization(request):
    sp = Specialization.objects.all()
    return render(request, 'visit/us.html', context={'sps':sp})

# @login_required
@sick_required
def sortdoctor(request, sp):
    drs = ProfileDoctor.objects.filter(expertise=sp)
    return render(request, 'visit/dr.html', context={'drs':drs})

# @login_required
@sick_required
def reserv(request, id):
    free_reservs = VisitTime.objects.filter(status='created').filter(doctor=id)
    return render(request, 'visit/visit.html', context={'free_reservs':free_reservs})

# @login_required
@sick_required
def detail_visit(request, id):
    visits = get_object_or_404(VisitTime, id=id)
    return render(request, 'visit/detail_visit.html', context={'visits':visits})


def visit_reserv(request, id):
    visit = get_object_or_404(VisitTime, id=id)
    user = ProfileSick.objects.get(user=request.user)
    visit.sick = user
    sick = user
    if sick.cash >= visit.specialization.cost:
        cash = sick.cash - visit.specialization.cost
        user.cash = cash
        user.save()
        visit.status = 'reserved'
        visit.save()
        return redirect('visit:sp')
    else:
        return HttpResponse('لطفا کیف پول خود را شارژ کنید .')

@login_required
@doctor_required
def list_visit_doctor(request):
    user = ProfileDoctor.objects.get(user=request.user)
    visits = VisitTime.objects.filter(doctor = user).filter(status = 'reserved')

    return render(request, 'visit/list_visit_dr.html', context={'visits':visits})

@login_required
@sick_required
def list_visit_sick(requset):
    user = ProfileSick.objects.get(user=requset.user)
    visits = VisitTime.objects.filter(sick=user).filter(status='reserved')

    return render(requset, 'visit/list_visit_sick.html', context={'visits':visits})

@login_required
def payment(request, id):
    user = get_object_or_404(ProfileSick, id=id)
    form = PaymentForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        cost = form.cleaned_data['cost']

        payment = form.save(commit=False)
        payment.user = user
        payment.save()
        user.cash += cost
        user.save()
        return redirect('/')
    else:
        form = PaymentForm()
    
    return render(request, 'visit/payment.html', {'form':form})
         
        
        
        
    
