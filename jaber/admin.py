from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Title)
admin.site.register(About)

class skillInline(admin.TabularInline):
  model = Skills
  extra = 2

@admin.register(Category)
class categoryAdmin(admin.ModelAdmin):
  inlines = [
    skillInline
  ]

admin.site.register(Projects)
admin.site.register(Social)