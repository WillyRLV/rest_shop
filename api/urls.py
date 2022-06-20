from django.urls import path

# importando vistas
from . import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('material', views.MaterialView.as_view()),
    path('funcion', views.FuncionView.as_view()),
]
