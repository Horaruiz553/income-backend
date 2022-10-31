from .views import PersonaView
from django.urls import path

urlpatterns=[
    path('personas/', PersonaView.as_view(), name='persona_list'),
    path('personas/<int:id>', PersonaView.as_view(), name='personas_process')
]