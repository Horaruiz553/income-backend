from .api import EgressApiView
from django.urls import path

urlpatterns=[
    path('egressAPI/', EgressApiView.as_view(), name='egressAPI'),
    path('egressAPI/<int:id>/<str:fecha>', EgressApiView.as_view(), name='egressAPIById')
]