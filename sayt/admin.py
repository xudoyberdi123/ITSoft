from django.contrib import admin
from .models import *


# Register your models here.


class ServiceUslugiAdmin(admin.StackedInline):
    model = ServicesUslugi


class ServiceAdmin(admin.ModelAdmin):
    inlines = [ServiceUslugiAdmin]

    class Meta:
        model = Services


admin.site.register(Category)
admin.site.register(Project)
admin.site.register(Services, ServiceAdmin)



