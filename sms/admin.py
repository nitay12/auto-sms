from django.contrib import admin

from .models import Employee, Service

admin.site.register(Employee)
admin.site.register(Service)