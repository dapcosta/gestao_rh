from django.urls import path, include
from .views import (
    DocumentoCreate,

)

urlpatterns = [
    path('novo/<int:funcionario_id>/', DocumentoCreate.as_view(), name='create_documento'),
    #path('deletar/<int:pk>/', DocumentoDelete.as_view(), name='create_departamento'),
]
