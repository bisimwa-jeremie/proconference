from django.urls import include, path

from .views import HelloAPIView

urlpatterns = [path("hello/", HelloAPIView.as_view())]
