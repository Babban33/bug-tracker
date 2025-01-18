from django.contrib import admin
from .models import Bug

@admin.register(Bug)
class BugAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'priority', 'assigned_to', 'created_at')
    search_fields = ('title', 'description')