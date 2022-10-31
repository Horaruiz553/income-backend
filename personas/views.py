from django.views.decorators.csrf import csrf_exempt
import json
from django.views import View
from .models import Persona
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator

# Create your views here.
class PersonaView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id>0):
            personas = list(Persona.objects.filter(id=id).values())
            if len(personas) > 0:
                datos = {"message": "success", "personas": personas[0]}
            else:
                datos = {"message": "Persona no encontrada"}
            return JsonResponse(datos) 
        else:
            personas = list(Persona.objects.values())
            if len(personas) > 0:
                datos = {"message": "success", "companies": personas}
            else:
                datos = {"message": "Persona no encontrada"}
            return JsonResponse(datos)    

    def post(self, request):
        jd = json.loads(request.body)
        Persona.objects.create(name=jd['name'], lastname=jd['lastname'], email=jd['email'])
        datos = {"message": "success"}
        return JsonResponse(datos)  

    def put(self, request, id):
        jd = json.loads(request.body)
        personas = list(Persona.objects.filter(id=id).values())
        if len(personas) > 0:
            persona = Persona.objects.get(id=id)
            persona.name = jd['name']
            persona.lastname = jd['lastname']
            persona.email = jd['email']

            persona.save()
            datos = {"message": "success"}
        else:
            datos = {"message": "Persona no encontrada"}
        return JsonResponse(datos)

    def delete(self, request, id):
        personas = list(Persona.objects.filter(id=id).values())
        if len(personas) > 0:
            Persona.objects.filter(id=id).delete()
            datos = {"message": "success"}
        else:
            datos = {"message": "Persona no encontrada"}
        return JsonResponse(datos)