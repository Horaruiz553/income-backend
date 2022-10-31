from django.views.decorators.csrf import csrf_exempt
import json
from django.views import View
from .models import User
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator

# Create your views here.
class UsersView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id>0):
            Users = list(User.objects.filter(id=id).values())
            if len(Users) > 0:
                datos = {"message": "success", "usuarios": Users[0]}
            else:
                datos = {"message": "Usuario no encontrada"}
            return JsonResponse(datos)
        else:
            Users = list(User.objects.values())
            if len(Users) > 0:
                datos = {"message": "success", "usuarios": Users}
            else:
                datos = {"message": "Usuarios no encontradas"}
            return JsonResponse(datos)

    def post(self, request, user=""):
        if (user == "LOGIN"):
            jd = json.loads(request.body)
            Users = list(User.objects.filter(usuario=jd['usuario'], contrasena=jd['contrasena']).values())
            if len(Users) > 0:
                datos = {"message": "success", "usuarios": Users[0]}
            else:
                datos = {"message": "Usuario no encontrada"}
            return JsonResponse(datos)
        else:
            jd = json.loads(request.body)
            User.objects.create(usuario=jd['usuario'], nombre=jd['nombre'], correo=jd['correo'], contrasena=jd['contrasena'])
            datos = {"message": "success"}
            return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        Users = list(User.objects.filter(id=id).values())
        if len(Users) > 0:
            UserReturn = User.objects.get(id=id)
            UserReturn.usuario = jd['usuario']
            UserReturn.nombre = jd['nombre']
            UserReturn.correo = jd['correo']
            UserReturn.contrasena = jd['contrasena']

            UserReturn.save()
            datos = {"message": "success"}
        else:
            datos = {"message": "Usuario no encontrado"}
        return JsonResponse(datos)

    def delete(self, request, id):
        Users = list(User.objects.filter(id=id).values())
        if len(Users) > 0:
            User.objects.filter(id=id).delete()
            datos = {"message": "success"}
        else:
            datos = {"message": "Usuario no encontrado"}
        return JsonResponse(datos)