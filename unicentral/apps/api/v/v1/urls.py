from django.urls import include, path

from .views import Univ_List_createview_upd_del, Cycle_list_creat,University_filters

create_cycle = Cycle_list_creat.as_view({"post":"create"})
list_cycle = Cycle_list_creat.as_view({"get":"list"})
update_cycle = Cycle_list_creat.as_view({"put":"update"})
delete_cycle = Cycle_list_creat.as_view({"delete":"delete"})
retraev_cycle = Cycle_list_creat.as_view({"get":"retrive"})
patch_cycle = Cycle_list_creat.as_view({'patch': 'partial_update'})
#for the cycle
create_univ = Univ_List_createview_upd_del.as_view({"post":"create"})
list_univ = Univ_List_createview_upd_del.as_view({"get":"list"})
update_univ = Univ_List_createview_upd_del.as_view({"put":"update"})
delete_univ = Univ_List_createview_upd_del.as_view({"delete":"delete"})
retraev_univ = Univ_List_createview_upd_del.as_view({"get":"retrive"})
patch_univ = Univ_List_createview_upd_del.as_view({'patch': 'partial_update'})

#ces url fonctionne correctement selon le besoin de de l'utilisateur en de modification
#en cas de modification ça ne repond pas correctement à tous les methode

urlpatterns = [path("cycle_create/", create_cycle, name="cycle_creat"),
                path("cycle_lite/", list_cycle, name="cycle_list"),
                path("cycle_update/", update_cycle, name="cycle_updat"),
                path("cycle_delete/", delete_cycle, name="cycle_delet"),
                path("cycle_patch/", patch_cycle, name="cycle_patch"),
                path("cycle_retrieve/",retraev_cycle, name="cycle_retriev"),

                #for cycle
                path("univ_create/", create_univ, name="univ_creat"),
                path("univ_liste/", list_univ, name="univ_list"),
                path("univ_update/", update_univ, name="univ_update"),
                path("univ_delete/", delete_univ, name="univ_delet"),
                path("univ_patch/", patch_univ, name="univ_patch"),
                path("univ_retrieve/",retraev_univ, name="univ_retreiv"),
                #for to filter the university
                path("univ_prov/", University_filters.as_view(), name="filter_uni"),
                 path("univ_prov/", University_filters.as_view(), name="filter_uni")


            ]
