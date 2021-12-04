from django.contrib import admin
from .models import Dictionaries

class DictAdmin(admin.ModelAdmin):

  list_display = ['inglizcha', 'uzbekcha']

admin.site.register(Dictionaries, DictAdmin)