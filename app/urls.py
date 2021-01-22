from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('', views.home, name="Home"),

    path('tienda/', views.tienda, name="Tienda"),
    path('contactos/', views.contactos, name="Contactos"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)