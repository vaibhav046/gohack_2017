from django.contrib import admin

# Register your models here.

from .models import Masterprofile,Profile,Transaction

admin.site.register(Masterprofile)
admin.site.register(Profile)
admin.site.register(Transaction)