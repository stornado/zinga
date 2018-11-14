from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Email)
admin.site.register(MailGroup)
admin.site.register(Schedule)
admin.site.register(Periodic)
