from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .tasks import send_relatorio

from apps.core.serializers import UserSerializer, GroupSerializer
from apps.funcionarios.models import Funcionario

@login_required
def home(request):
    data = {}
    data['usuario'] = request.user
    return render(request, 'core/index.html', data)

def celery(request):
    send_relatorio()
    return HttpResponse('Tarefa incluida na fila para execução')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer