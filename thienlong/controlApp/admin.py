from django.contrib import admin
from .models import control, pen_show,test

class contorAdmin(admin.ModelAdmin):
    list_display = ['id','size','speed','state']

class TestAdmin(admin.ModelAdmin):
    list_display = ['id','sizepaper','speed','error','state']

class ResultAdmin(admin.ModelAdmin):
    list_display = ['id','avg_pen','dotted_lenght','distance','state','time']
# Register your models here.
admin.site.register(control,contorAdmin)
admin.site.register(pen_show,ResultAdmin)