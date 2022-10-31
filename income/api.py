import datetime
from datetime import date

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from income.models import Income
from income.serializer import IncomeSerializer, TestIncomeSerializer


class IncomeApiView(APIView):

    def get(self, request, id=0, fecha="--"):
        # Solo de prueba
        #test_data = {'name': 'Horacio', 'email': 'horacioruizd@gmail.com'}
        #test_income = TestIncomeSerializer(data=test_data, context=test_data)
        #if test_income.is_valid():
        #    print('Pasó las validaciones')
        #else:
        #    print(test_income.errors)
        if (id > 0):
            income = Income.objects.filter(id=id).first()
            income_serializer = IncomeSerializer(income)
            return Response(income_serializer.data, status=status.HTTP_200_OK)
        if (fecha != "--"):
            x = fecha.split("-")
            income = Income.objects.filter(fecha__year=x[0], fecha__month=x[1])
            income_serializer = IncomeSerializer(income, many=True)
            return Response(income_serializer.data, status=status.HTTP_200_OK)
        else:
            income = Income.objects.all()
            income_serializer = IncomeSerializer(income, many=True)
            return Response(income_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        income_serializer = IncomeSerializer(data=request.data)
        if income_serializer.is_valid():
            income_serializer.save()
            return Response(income_serializer.data, status=status.HTTP_201_CREATED)
        return Response(income_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        income = Income.objects.filter(id=id).first()
        if income:
            income_serializer = IncomeSerializer(income, data=request.data)
            if income_serializer.is_valid():
                income_serializer.save()
                return Response(income_serializer.data, status=status.HTTP_200_OK)
            return Response(income_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Ingreso no encontrado!.'}, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        income = Income.objects.filter(id=id).first()
        if income:
            income.delete()
            return Response({'message': 'Usuario eliminado correctamente!.'}, status=status.HTTP_200_OK)
        return Response({'message': 'Ingreso no encontrado!.'}, status=status.HTTP_400_BAD_REQUEST)