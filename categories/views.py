from django.views.decorators.csrf import csrf_exempt
import json
from django.views import View
from .models import Categorie
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator

# Create your views here.
class CategoriesView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id>0):
            Categories = list(Categorie.objects.filter(id=id).values())
            if len(Categories) > 0:
                datos = {"message": "success", "categorias": Categories[0]}
            else:
                datos = {"message": "Categoria no encontrada"}
            return JsonResponse(datos) 
        else:
            Categories = list(Categorie.objects.values())
            if len(Categories) > 0:
                datos = {"message": "success", "categorias": Categories}
            else:
                datos = {"message": "Categorias no encontradas"}
            return JsonResponse(datos)

    def get(self, request, tipo=""):
        if(tipo == "ingreso"):
            Categories = list(Categorie.objects.filter(ingreso=True).values())
            if len(Categories) > 0:
                datos = {"message": "success", "categorias": Categories}
            else:
                datos = {"message": "Categoria no encontrada"}
            return JsonResponse(datos)
        else:
            Categories = list(Categorie.objects.filter(ingreso=False).values())
            if len(Categories) > 0:
                datos = {"message": "success", "categorias": Categories}
            else:
                datos = {"message": "Categoria no encontrada"}
            return JsonResponse(datos)

    def post(self, request):
        jd = json.loads(request.body)
        Categorie.objects.create(descripcion=jd['descripcion'], ingreso=jd['ingreso'])
        datos = {"message": "success"}
        return JsonResponse(datos)  

    def put(self, request, id):
        jd = json.loads(request.body)
        Categories = list(Categorie.objects.filter(id=id).values())
        if len(Categories) > 0:
            CategorieReturn = Categorie.objects.get(id=id)
            CategorieReturn.descripcion = jd['descripcion']
            CategorieReturn.ingreso = jd['ingreso']

            CategorieReturn.save()
            datos = {"message": "success"}
        else:
            datos = {"message": "Companies not found"}
        return JsonResponse(datos)

    def delete(self, request, id):
        Categories = list(Categorie.objects.filter(id=id).values())
        if len(Categories) > 0:
            Categorie.objects.filter(id=id).delete()
            datos = {"message": "success"}
        else:
            datos = {"message": "Categoria no encontrada"}
        return JsonResponse(datos)