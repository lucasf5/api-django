from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'clientes', views.ClientesViewSet)
router.register(r'empresas', views.EmpresasViewSet)
router.register(r'associacao', views.AssociacaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('associacao/<int:pk>/cliente', views.AssociacaoClienteSerializerViewSet.as_view()),
    path('associacao/<int:pk>/empresa', views.AssociacaoEmpresaSerializerViewSet.as_view()),
]
