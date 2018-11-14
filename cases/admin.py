from django.contrib import admin

from .models import Business, Product, Module, Tag, ZentaoCase

# Register your models here.

admin.site.register(Business)
admin.site.register(Product)
admin.site.register(Module)
admin.site.register(ZentaoCase)
admin.site.register(Tag)
