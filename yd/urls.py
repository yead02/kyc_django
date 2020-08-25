from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('Govt_Acc', views.gov),
    path('Fixed_Deposit', views.fixd),
    path('Individual', views.ind),
    path('non-individual', views.nind),
    path('fxd_add', views.fxd_add),
]
