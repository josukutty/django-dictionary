from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('dict',views.dict,name='dictionary')
]