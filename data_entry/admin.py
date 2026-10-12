from django.contrib import admin
from . import models 



@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','roll_number','age']
    search_fields=['name','roll_number']
    
admin.site.register(models.Customer)