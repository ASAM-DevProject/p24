from statistics import mode
from django.db import models
from acc.models import ProfileDoctor, ProfileSick
# Create your models here.



class Specialization(models.Model):
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL, related_name='childern', verbose_name='تخصص')
    title = models.CharField(max_length=255, verbose_name='عنوان تخصص')
    cost = models.IntegerField(verbose_name='هزینه')
    slug = models.SlugField(max_length=255, unique=True, allow_unicode=True, verbose_name='لینک کوتاه')

    def __str__(self):
        return f'تخصص :: {self.title}, هزینه :: {self.cost}'
    
class VisitTime(models.Model):
    STATUS = (
        ('created','created'),
        ('reserved','reserved'),
        ('canseled','canceld'),
        ('done', 'done'),
    )
    specialization = models.ForeignKey(to=Specialization,on_delete=models.CASCADE)
    date = models.DateField("Date")
    time = models.TimeField("Time")
    doctor = models.ForeignKey(to=ProfileDoctor, on_delete=models.CASCADE)
    sick = models.ForeignKey(to=ProfileSick, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=20, default='created',choices=STATUS)
    count = models.IntegerField('count')

    def __str__(self):
        return f'{self.doctor.first_name} {self.doctor.last_name} / تخصص :: {self.specialization.title}'

class Payment(models.Model):
    user = models.ForeignKey(to=ProfileSick, on_delete=models.PROTECT)
    cost = models.IntegerField(verbose_name='مبلغ شارژ حساب')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} , هزینه :: {self.cost}'

    