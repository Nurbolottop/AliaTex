from django.contrib import admin
from apps.cms import models as cms_models
from django.utils.html import format_html

# Register your models here.

@admin.register(cms_models.Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slogan',  'email', 'phone', 'work_schedule', 'logo_preview', 'icon_preview')
    list_display_links = ('title',)
    search_fields = ('title', 'description', 'email', 'phone')
    readonly_fields = ('logo_preview', 'icon_preview')

    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'slogan', 'slogan_description', 'description', 'logo', 'logo_preview', 'icon', 'icon_preview')
        }),
        ('Контактная информация', {
            'fields': ('email', 'phone', 'work_schedule','locate')
        }),
        ('Социальные сети', {
            'fields': ('whatsapp', 'telegram', 'instagram', 'facebook'),
            'classes': ('collapse',)
        }),
    )

    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" style="max-height:50px;max-width:100px;" />', obj.logo.url)
        return "-"
    logo_preview.short_description = "Логотип (превью)"
    logo_preview.allow_tags = True

    def icon_preview(self, obj):
        if obj.icon:
            return format_html('<img src="{}" style="max-height:50px;max-width:100px;" />', obj.icon.url)
        return "-"
    icon_preview.short_description = "Иконка (превью)"
    icon_preview.allow_tags = True

    def has_add_permission(self, request):
        # Запрещаем создание новых объектов Settings если уже есть хотя бы один
        return not cms_models.Settings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Запрещаем удаление объекта Settings
        return False

@admin.register(cms_models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'preview_image', 'short_description')
    list_display_links = ('title',)
    search_fields = ('title', 'descriptions')
    readonly_fields = ('preview_image',)
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'category', 'descriptions')
        }),
        ('Изображение', {
            'fields': ('image', 'preview_image'),
            'description': 'Рекомендуемый формат изображения: WEBP, качество: 100%'
        }),
    )
    
    def preview_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 50px; border-radius: 5px;" />', obj.image.url)
        return 'Нет изображения'
    
    def short_description(self, obj):
        return obj.descriptions[:50] + '...' if len(obj.descriptions) > 50 else obj.descriptions
    
    preview_image.short_description = 'Предпросмотр'
    short_description.short_description = 'Краткое описание'

    class Media:
        css = {
            'all': ('admin/css/custom.css',)
        }

@admin.register(cms_models.Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'preview_image')
    list_display_links = ('title',)
    search_fields = ('title', 'subtitle')
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'subtitle')
        }),
        ('Изображение', {
            'fields': ('image',)
        }),
    )
    
    def preview_image(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="max-height: 50px;"/>'
        return 'Нет изображения'
    
    preview_image.short_description = 'Предпросмотр'
    preview_image.allow_tags = True
    
@admin.register(cms_models.Partners)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('preview_image', 'url')
    list_display_links = ('url',)
    search_fields = ('url',)
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('url',)
        }),
        ('Изображение', {
            'fields': ('image',)
        }),
    )
    
    def preview_image(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="max-height: 50px;"/>'
        return 'Нет изображения'
    
    preview_image.short_description = 'Предпросмотр'
    preview_image.allow_tags = True
