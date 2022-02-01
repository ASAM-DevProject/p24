from django.urls import path
from visit.views import (create_visit_table, specialization, sortdoctor, reserv, 
                        detail_visit, visit_reserv, list_visit_doctor, list_visit_sick, payment)

app_name='visit'

urlpatterns = [
    path('DCVF/',create_visit_table, name='create_visit_table'),

    path('sp/', specialization, name='sp'),
    path('dr/<int:sp>/', sortdoctor, name='dr'),
    path('visit/<int:id>', reserv, name='reserv'),
    path('visit/detail/<int:id>/', detail_visit, name='detail_visit'),
    path('reserv/<int:id>/', visit_reserv, name='reserv_visit'),
    path('account/profile/visits/dr', list_visit_doctor, name='list_visit_dr'),
    path('account/profile/visits/sick', list_visit_sick, name='list_visit_sick'),
    path('account/payment/<int:id>/', payment, name='payment')
]
