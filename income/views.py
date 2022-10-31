from django.views.decorators.csrf import csrf_exempt
import json
from django.views import View
from .models import Income
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator

# Create your views here.
class IncomesView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id>0):
            Incomes = list(Income.objects.filter(id=id).values())
            if len(Incomes) > 0:
                datos = {"message": "success", "ingresos": Incomes[0]}
            else:
                datos = {"message": "Ingreso no encontrado"}
            return JsonResponse(datos) 
        else:
            Incomes = list(Income.objects.values())
            if len(Incomes) > 0:
                datos = {"message": "success", "ingresos": Incomes}
            else:
                datos = {"message": "Ingresos no encontrados"}
            return JsonResponse(datos)    

    def post(self, request):
        jd = json.loads(request.body)
        Income.objects.create(idusuario_id=jd['idusuario'], idcategoria_id=jd['idcategoria'],
                              fecha=jd['fecha'], descripcion=jd['descripcion'], monto=jd['monto'])
        datos = {"message": "success"}
        return JsonResponse(datos)  

    def put(self, request, id):
        Incomes = list(Income.objects.filter(id=id).values())
        jd = json.loads(request.body)
        if len(Incomes) > 0:
            IncomeReturn = Income.objects.get(id=id)
            IncomeReturn.idusuario_id = jd['idusuario']
            IncomeReturn.idcategoria_id = jd['idcategoria']
            IncomeReturn.fecha = jd['fecha']
            IncomeReturn.descripcion = jd['descripcion']
            IncomeReturn.monto = jd['monto']

            IncomeReturn.save()
            datos = {"message": "success"}
        else:
            datos = {"message": "Ingreso no encontrado"}
        return JsonResponse(datos)

    def delete(self, request, id):
        Incomes = list(Income.objects.filter(id=id).values())
        if len(Incomes) > 0:
            Income.objects.filter(id=id).delete()
            datos = {"message": "success"}
        else:
            datos = {"message": "Ingreso no encontrada"}
        return JsonResponse(datos)