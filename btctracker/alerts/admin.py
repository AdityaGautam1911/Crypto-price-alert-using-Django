from django.contrib import admin
from .models import Alert


@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ('price', 'alert_date_and_time')
    list_filter = ('alert_date_and_time',)
    search_fields = ('price',)
