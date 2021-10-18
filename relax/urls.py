from django.urls import path
from . import views

urlpatterns = [
    path('tets/', views.test, name="test"),
    
]