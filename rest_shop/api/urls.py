from django.urls import path

# importando vistas
from . import views

urlpatterns = [
    path('', views.IndexView.as_view()),
]
