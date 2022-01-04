from django.urls import path 

urlspatterns = [
    path('registrar/', RegistrarUsuarioView.as_view(), name='registrar')
]