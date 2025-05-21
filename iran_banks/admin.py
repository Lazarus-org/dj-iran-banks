from django.contrib import admin
from .models import Bank

@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'active', 'updated_at')
    list_filter = ('active',)
    search_fields = ('name', 'code')
    ordering = ('name',)

