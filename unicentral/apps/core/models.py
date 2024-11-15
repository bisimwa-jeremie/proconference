from django.db import models
from django.conf import settings
from django.utils import timezone


class BaseQueryset(models.QuerySet):
    def delete(self, **kwargs):
        return super().update(deleted_at=timezone.now())
    

class BaseManager(models.Manager):
    def get_queryset(self):
        return BaseQueryset(self.model, using=self._db).filter(deleted_at=None)


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, 
                        on_delete=models.SET_NULL, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    objects = BaseManager()

    class Meta:
        abstract = True

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()
