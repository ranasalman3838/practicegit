from django.contrib import admin
from .models import *

# Register your models her
class employeeset(admin.ModelAdmin):
    list_display = ('first_name','last_name','email','gender','office')
class officeset(admin.ModelAdmin):
    list_display = ('name','location')

admin.site.register(Employee,employeeset)
admin.site.register(Office,officeset)