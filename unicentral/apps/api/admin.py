from django.contrib import admin

from .models import (University, Cycle, Faculty, Candidate,
                    Departement, Article, Discussion, Response,
                    Nationnality)


class UniversityAdmin(admin.ModelAdmin):
    list_display = '__all__'

class CycleAdmin(admin.ModelAdmin):
    list_display = '__all__'

class FacultyAdmin(admin.ModelAdmin):
    list_display = '__all__'

class DepartmentAdmin(admin.ModelAdmin):
    list_display = '__all__'

class NationnalityAdmin(admin.ModelAdmin):
    list_display = '__all__'

class CandiateAdmin(admin.ModelAdmin):
    list_display = '__all__'

class ArticleAdmin(admin.ModelAdmin):
    list_display = '__all__'

class DiscussionAdmin(admin.ModelAdmin):
    list_display = '__all__'

class ResponseAdmin(admin.ModelAdmin):
    list_display = '__all__'


# Enregistrement des tous les modeles dans l'administration


admin.site.register(University, UniversityAdmin)
admin.site.register(Cycle, CycleAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Departement, DepartmentAdmin)
admin.site.register(Nationnality, NationnalityAdmin)
admin.site.register(Candidate, CandiateAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Discussion, DiscussionAdmin)
admin.site.register(Response, ResponseAdmin)