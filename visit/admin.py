from django.contrib import admin
from acc.models import ProfileDoctor, ProfileSick,User
from visit.models import VisitTime,Specialization, Payment
# Register your models here.

admin.site.register(ProfileDoctor)
admin.site.register(ProfileSick)
admin.site.register(User)
admin.site.register(VisitTime)
admin.site.register(Specialization)
admin.site.register(Payment)






