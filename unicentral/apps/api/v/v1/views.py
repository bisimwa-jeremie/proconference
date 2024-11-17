from django.contrib.auth.models import Permission
from rest_framework.generics import ListAPIView
from rest_framework.permissions import BasePermission
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from unicentral.apps.api.models import University, Cycle
from unicentral.apps.api.serializers import UniversitySerializer, CycleSerializer



   # This ViewSet automatically provides `list`, `create`, `retrieve`,
    #`update` and `destroy` actions.

   # Additionally we also provide an extra `highlight` action.
  
class Univ_List_createview_upd_del(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer

class Cycle_list_creat(viewsets.ModelViewSet):
    serializer_class = CycleSerializer
    queryset = Cycle.objects.all()

# for to filter the univrsity at thr pronvinces
class University_filters(ListAPIView):
    serializer_class=UniversitySerializer
    filter_backends= [SearchFilter]
    searching = ['province']

class University_filters(ListAPIView):
    serializer_class=CycleSerializer
    filter_backends= [SearchFilter]
    searching_cycle = ['university']