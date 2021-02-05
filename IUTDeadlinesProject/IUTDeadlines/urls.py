from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('freshman', views.freshman, name='freshman'),
    path('junior', views.junior, name='junior'),
    path('senior', views.senior, name='senior')
]
