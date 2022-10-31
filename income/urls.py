from .api import IncomeApiView
from .views import IncomesView
from django.urls import path

urlpatterns=[
    path('incomes/', IncomesView.as_view(), name='income_list'),
    path('incomes/<int:id>', IncomesView.as_view(), name='incomes_process'),
    path('incomesAPI/', IncomeApiView.as_view(), name='incomesAPI'),
    path('incomesAPI/<int:id>/<str:fecha>', IncomeApiView.as_view(), name='incomesAPIById')
]