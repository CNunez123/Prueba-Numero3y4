from django.contrib import admin
from django.urls import path
from seminario import views
from seminario.views import home, InscritoList, InscritoDetail, InstitucionList, InstitucionDetail, agregar_inscrito, agregar_institucion
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('inscritos/', views.inscritos_list, name='inscritos-list'),
    path('inscritos/agregar/', views.agregar_inscrito, name='agregar-inscrito'),
    path('instituciones/', views.instituciones_list, name='instituciones-list'),
    path('instituciones/agregar/', views.agregar_institucion, name='agregar-institucion'),
    path('api/inscritos/', views.InscritoList.as_view(), name='api-inscritos-list'),
    path('api/inscritos/<int:pk>/', views.InscritoDetail.as_view(), name='api-inscrito-detail'),
    path('api/instituciones/', views.InstitucionList.as_view(), name='api-instituciones-list'),
    path('api/instituciones/<int:pk>/', views.InstitucionDetail.as_view(), name='api-institucion-detail'),
    path('instituciones/', InstitucionList.as_view(), name='instituciones-list'),
    path('instituciones/<int:pk>/', InstitucionDetail.as_view(), name='institucion-detail'),
    path('inscritos/', InscritoList.as_view(), name='inscritos-list'),
    path('inscritos/<int:pk>/', InscritoDetail.as_view(), name='inscrito-detail'),
]
