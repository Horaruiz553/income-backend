from rest_framework import serializers

from categories.models import Categorie
from categories.serializer import CategorieSerializer
from egress.models import Egress
from users.models import User
from users.serializer import UserSerializer


class EgressSerializer(serializers.ModelSerializer):
    #Esto es para trabaar sin el to_representation()
    #idusuario = UserSerializer()
    #idcategoria = CategorieSerializer()
    class Meta:
        model = Egress
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

