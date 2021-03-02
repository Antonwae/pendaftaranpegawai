from django.urls import path
from .import views

urlpatterns=[
    path('',views.dashboard),
    path('pengisianform/',views.pengisianform),
    path('tampilan/',views.tampilan)
]