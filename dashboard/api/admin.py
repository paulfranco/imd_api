from django.contrib import admin
from .models import Settlement, Carrier

@admin.register(Settlement)
class SettlementAdmin(admin.ModelAdmin):
    fields = ('title', 'settlement_type', 'start_date', 'end_date', 'quarter', 'year', 'stop_count', 'route_count', 'revenue', 'check_number', 'paid', 'carrier')
    list_display = ['title', 'settlement_type', 'start_date', 'end_date', 'quarter', 'year', 'stop_count', 'route_count', 'revenue', 'check_number', 'paid', 'carrier']
    search_fields = ('title', 'date_end')

@admin.register(Carrier)
class CarrierAdmin(admin.ModelAdmin):
    fields = ('company_name', 'user')
    list_display = ['user']
    search_fields = ('user',)