"""nucleos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from aplicacion import views
from aplicacion.token import login

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.home, name="home"),
    path('', login.as_view(), name= 'login'),
    path('registro/', views.registro, name="registro"),
    path('autenticacion/', views.autenticacion, name="autenticacion"),
    path('nucleos/', views.nucleos, name="nucleos"),
    path('integrantes/', views.integrantes, name="integrantes"),
    path('detalle/', views.detalle, name="detalle"),
    path('crear_nucleos/', views.crear_nucleo, name="crear_nucleo"),
    path('eliminar/nucleos/<int:user_id>/', views.eliminar_nucleo, name="eliminar_nucleo"),
    path('eliminar/integrantes/<int:int_id>/', views.eliminar_integrante, name="eliminar_integrante"),
    path('actualizar/integrantes/<int:act_id>/', views.actualizar_integrantes, name="actualizar_integrante"),
    path('casos/<int:id>/', views.casos, name="casos"),
    path('eliminar/usuario/', views.eliminar_usuario, name="eliminar_usuario"),
    path('cerrar/', views.cerrar, name="cerrar"),
]
