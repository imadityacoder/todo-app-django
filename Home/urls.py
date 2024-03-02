from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>/delete', views.delete, name='delete'),
    path('<int:id>/update', views.update, name='update'),
]