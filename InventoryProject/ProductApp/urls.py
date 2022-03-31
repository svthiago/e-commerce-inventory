from django.conf.urls import url
from ProductApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [ 
    url(r'^product$', views.productApi),
    url(r'^product/([0-9]+)$', views.productApi),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)