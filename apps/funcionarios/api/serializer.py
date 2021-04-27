from rest_framework import serializers

from apps.funcionarios.models import Funcionario
from apps.registro_horas_extras.api.serializer import RegistroHoraExtraSerializer


class FuncionarioSerializer(serializers.ModelSerializer):
    registrohoraextra_set = RegistroHoraExtraSerializer(many=True)
    class Meta:
        model = Funcionario
        fields = ['id', 'nome', 'departamentos', 'empresa', 'user', 'imagem', 'total_horas_extra', 'registrohoraextra_set']