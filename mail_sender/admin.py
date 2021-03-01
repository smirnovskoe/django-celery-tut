from django.contrib import admin

from . import models


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',)


@admin.register(models.TestModel)
class TestAdmin(admin.ModelAdmin):
    list_display = ('status', 'date_start',)
