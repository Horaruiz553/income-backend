from .views import CategoriesView  
from django.urls import path

urlpatterns=[
    path('categories/', CategoriesView.as_view(), name='categorie_list'),
    path('categories/<int:id>', CategoriesView.as_view(), name='categories_process'),
    path('categories/<str:tipo>', CategoriesView.as_view(), name='categories_tipo')
]