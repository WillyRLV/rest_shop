from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Material
from .serializers import MaterialSerializer
from .models import Funcion
from .serializers import FuncionSerializer



class IndexView(APIView):
    def get(self,request):
        context = {
            'ok':True,
            'message':'el servidor esta activo!'
        }
        return Response(context)


class MaterialView(APIView):
    def get (self,request):
        dataMaterial = Material.objects.all()
        serMaterial = MaterialSerializer(dataMaterial,many=True)
        context = {
            'ok':True,
            'content':serMaterial.data
        }

        return Response(context)


class FuncionView(APIView):
    def get (self,request):
        dataFuncion = Funcion.objects.all()
        serFuncion = FuncionSerializer(dataFuncion,many=True)
        context = {
            'ok':True,
            'content':serFuncion.data
        }

        return Response(context)