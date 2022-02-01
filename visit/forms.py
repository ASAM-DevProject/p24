from django.forms import ModelForm

from visit.models import VisitTime, Payment



class CreateVisitTImeForm(ModelForm):
    class Meta:
        model = VisitTime
        fields = ['date','time','count']
        
class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = ['cost']