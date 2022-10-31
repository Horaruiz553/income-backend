from rest_framework import serializers

from categories.serializer import CategorieSerializer
from income.models import Income
from users.serializer import UserSerializer


class IncomeSerializer(serializers.ModelSerializer):
    #idusuario = UserSerializer()
    #idcategoria = CategorieSerializer()
    class Meta:
        model = Income
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'idusuario': instance.idusuario.nombre,
            'idcategoria': instance.idcategoria.descripcion,
            'fecha': instance.fecha,
            'descripcion': instance.descripcion,
            'monto': instance.monto,
        }

class TestIncomeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()

    def validate_name(self, value):
        #Custom validation
        if 'z' in value:
            raise serializers.ValidationError("Error, el campo nombre no debe quedar vacio")
        print(value)
        print(self.context['email'])
        return value

    def validate_email(self, value):
        print(value)
        print(self.context['name'])
        return value

    def validate(self, data):
        print("Ultima validacion")
        return data