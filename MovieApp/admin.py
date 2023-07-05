from django.contrib import admin

from . import models
# Register your models here.
class customCustomer(admin.ModelAdmin):
    list_display = ['email','username']
    # readonly_fields = ('password',)

class customMovie(admin.ModelAdmin):
    list_display=['movie_name','movie_desc']
    

class customShow(admin.ModelAdmin):
    list_display = ['movie','Timing','seats']
    list_display_links = ['movie']
    display_field = 'movie_name'

class employee_admin(admin.ModelAdmin):
    list_display=['employeeName','designation']

admin.site.register(models.Customer,customCustomer)
admin.site.register(models.movies,customMovie)
admin.site.register(models.show,customShow)
admin.site.register(models.employee,employee_admin)