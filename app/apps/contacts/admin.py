from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'is_published')
    list_filter = ('created_at', 'is_published')
    search_fields = ('name', 'review_text')
    ordering = ('-created_at',)
    list_per_page = 20
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'review_text', 'is_published')
        }),
        ('Дополнительная информация', {
            'fields': ('created_at',)
        }),
    )
    
    readonly_fields = ('created_at',)
    
    def has_delete_permission(self, request, obj=None):
        return True
    
    def has_change_permission(self, request, obj=None):
        return True
    
    def has_add_permission(self, request):
        return True
    
    class Media:
        css = {
            'all': ('admin/css/custom.css',)
        }
