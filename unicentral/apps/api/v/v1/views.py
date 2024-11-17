from django.contrib.auth.models import Permission
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import BasePermission
from rest_framework import viewsets
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

#class Retriev_update_delete(RetrieveUpdateDestroyAPIView):
    # serializer_class = CycleSerializer

   # def get_queryset(self):
      #  return Cycle.objects.filter(pk=self.kwargs.get("pk"))

    #def delete_cycle(self):
        #return Cycle.objects.select_related(university=self.kwargs.get("university"))