from django.urls import path

# importando vistas
from . import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('material', views.MaterialView.as_view()),
    path('funcion', views.FuncionView.as_view()),
    path('producto', views.ProductoView.as_view()),
    path('material/<int:material_id>/productos', views.MaterialProductosView.as_view()),
    path('contacto', views.ContactoView.as_view()),
]
