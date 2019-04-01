from django.contrib import admin
from quick.ninja.models import Nija
# Register your models here.
@admin.register(Nija)
class NijaAdmin(admin.ModelAdmin):
    list_display = ["first_name","last_name","gender"]




 