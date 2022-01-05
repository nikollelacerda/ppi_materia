from django.urls import path
from usuarios.views import RegistrarUsuarioView

urlspatterns = [
    path('registrar/', RegistrarUsuarioView.as_view(), name='registrar')
]