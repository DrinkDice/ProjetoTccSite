from django.contrib import admin
from .models import Instrumentos, Usuario
from django.contrib.auth.admin import UserAdmin
# Register your models here.

# só exite porque queremeos que no admin apareça o campo personalizado instrumentos_vistos
campos = list(UserAdmin.fieldsets)
campos.append(
    ("Histórico", {'fields': ('instrumentos_vistos',)})
)
UserAdmin.fieldsets = tuple(campos)

admin.site.register(Instrumentos)
admin.site.register(Usuario, UserAdmin)

