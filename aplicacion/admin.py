from django.contrib import admin
from .models import *
from .token import Token

# Register your models here.

admin.site.register(Nucleos)
admin.site.register(Integrantes)
admin.site.register(DatosPersonales)
admin.site.register(Token)