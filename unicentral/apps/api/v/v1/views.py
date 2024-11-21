from http import HTTPMethod
#from django.contrib.auth.models import Permission
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import viewsets
from unicentral.apps.api.models import University, Cycle
from unicentral.apps.api.serializers import UniversitySerializer, CycleSerializer
#from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

   # This ViewSet automatically provides `list`, `create`, `retrieve`,
    #`update` and `destroy` actions.

   # Additionally we also provide an extra `highlight` action.
  
class Univ_List_createview_upd_del(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    #permission_classes = (IsAuthenticated,)
    filterset_fields = ['adress','province', 'country']
    #filter_backends= [SearchFilter] // ce champ, je l'ai definis dans le settings [SearchFilter] 
    search_fields = ['name','province','country']
    
    # def destory(self,request, *args, **kwargs):
    #     supp = self.get_queryset()
    #     supp.delete()
    #     return Response({"reponse":"Your deleting was success"}, status=status.HTTP_204_NO_CONTENT)
    
    # def update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=400)

    # def partial_update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=400)

class Cycle_list_creat(viewsets.ModelViewSet):
    serializer_class = CycleSerializer
    queryset = Cycle.objects.all()
    #permission_classes = (IsAuthenticated)
    filterset_fields = ['university','cycle']
    #filter_backends= [SearchFilter] // ce champs je l'ai definis dans le settings [SearchFilter]
    search_fields = ['university','clycle']
    lookup_field = 'id'

  