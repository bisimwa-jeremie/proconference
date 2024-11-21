from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import Univ_List_createview_upd_del, Cycle_list_creat


router = DefaultRouter()
router.register("university", Univ_List_createview_upd_del)
router.register("cyles",Cycle_list_creat)
urlpatterns = [
    path("", include(router.urls)),

             
]