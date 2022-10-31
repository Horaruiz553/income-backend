from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from egress.models import Egress
from egress.serializer import EgressSerializer


class EgressApiView(APIView):
    def get(self, request, id=0, fecha=""):
        if(id>0):
            egress = Egress.objects.filter(id=id).first()
            egress_serializer = EgressSerializer(egress)
            return Response(egress_serializer.data, status=status.HTTP_200_OK)
        if (fecha != "--"):
            x = fecha.split("-")
            income = Egress.objects.filter(fecha__year=x[0], fecha__month=x[1])
            income_serializer = EgressSerializer(income, many=True)
            return Response(income_serializer.data, status=status.HTTP_200_OK)
        else:
            egress = Egress.objects.all()
            egress_serializer = EgressSerializer(egress, many=True)
            return Response(egress_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        egress_serializer = EgressSerializer(data=request.data)
        if egress_serializer.is_valid():
            egress_serializer.save()
            return Response(egress_serializer.data, status=status.HTTP_201_CREATED)
        return Response(egress_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        egress = Egress.objects.filter(id=id).first()
        if egress:
            egress_serializer = EgressSerializer(egress, data=request.data)
            if egress_serializer.is_valid():
                egress_serializer.save()
                return Response(egress_serializer.data, status=status.HTTP_200_OK)
            return Response(egress_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Ingreso no encontrado!.'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        egress = Egress.objects.filter(id=id).first()
        if egress:
            egress.delete()
            return Response({'message': 'Usuario eliminado correctamente!.'}, status=status.HTTP_200_OK)
        return Response({'message': 'Ingreso no encontrado!.'}, status=status.HTTP_400_BAD_REQUEST)