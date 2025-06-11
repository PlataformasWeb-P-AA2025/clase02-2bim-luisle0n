from django.contrib import admin

# Importar las clases del modelo
from app1.models import Estudiante , Ciudad

admin.site.register(Estudiante)
admin.site.register(Ciudad)