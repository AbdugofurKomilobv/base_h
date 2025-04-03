from django.contrib import admin


from .models import *

class TemUs(admin.ModelAdmin):
    list_display = ['name','target','info','img','created_at']

admin.site.register(Testimonials,TemUs)



