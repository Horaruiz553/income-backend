from .views import UsersView
from django.urls import path

urlpatterns=[
    path('usuarios/', UsersView.as_view(), name='usuario_list'),
    path('usuarios/<int:id>', UsersView.as_view(), name='usuario_process'),
    path('usuarios/<str:user>/', UsersView.as_view(), name='usuario_login')
]