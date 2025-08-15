from django.contrib import admin
from django import forms
from apps.index import models as index_models
from django.utils.html import format_html, mark_safe

class AboutServiceInlineForm(forms.ModelForm):
    # Use the same icon choices as Numbers to keep consistency
    icon = forms.ChoiceField(choices=index_models.Numbers.ICON_CHOICES, required=False, label='Иконка')

    class Meta:
        model = index_models.AboutService
        fields = '__all__'

class AboutServiceInline(admin.TabularInline):
    model = index_models.AboutService
    extra = 1
    form = AboutServiceInlineForm
    fields = ('title', 'subtitle', 'icon')

@admin.register(index_models.About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'experience', 'service_count')
    list_display_links = ('title',)
    search_fields = ('title', 'descriptions')
    inlines = [AboutServiceInline]
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'descriptions', 'experience')
        }),
   
    )

    def service_count(self, obj):
        return obj.about_service.count()
    service_count.short_description = 'Количество услуг'

    def has_add_permission(self, request):
        # Запрещаем создание новых объектов About если уже есть хотя бы один
        return not index_models.About.objects.exists()
    

@admin.register(index_models.Numbers)
class NumbersAdmin(admin.ModelAdmin):
    list_display = ('title',  'number', 'short_description', 'preview_image')
    list_display_links = ('title',)
    search_fields = ('title', 'descriptions')
    readonly_fields = ('preview_icon',)
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'number', 'descriptions')
        }),
        ('Изображение и иконка', {
            'fields': ('image', ('icon', 'preview_icon')),
            'description': 'Выберите иконку из списка. Предпросмотр появится после сохранения.'
        }),
    )
    
    def preview_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 50px; border-radius: 5px;"/>', obj.image.url)
        return 'Нет изображения'
    
    def preview_icon(self, obj):
        icons_preview = []
        for value, label in index_models.Numbers.ICON_CHOICES:
            selected = 'border: 2px solid #447e9b;' if obj and obj.icon == value else ''
            icons_preview.append(
                format_html(
                    '<div style="display: inline-block; margin: 5px; padding: 10px; cursor: pointer; background-color: #f5f5f5; border-radius: 5px; {}" '
                    'onclick="document.getElementById(\'id_icon\').value=\'{}\';">' 
                    '<span class="{}" style="font-size: 32px; color: #333; display: block; text-align: center;"></span>'
                    '<div style="font-size: 12px; margin-top: 8px; text-align: center; color: #000;">{}</div>'
                    '</div>',
                    selected, value, value, label
                )
            )
        
        return format_html(
            '<style>'
            '[class^="flaticon-"]:before, [class*=" flaticon-"]:before {{ font-family: flaticon !important; }}'
            '</style>'
            '<div style="margin-top: 10px;">'
            '<div style="margin-bottom: 10px; font-weight: bold;">Нажмите на иконку для выбора:</div>'
            '<div style="display: flex; flex-wrap: wrap; gap: 15px; padding: 15px; background-color: white; border-radius: 8px;">'
            '{}'
            '</div>'
            '</div>',
            mark_safe(''.join(icons_preview))
        )
    
    def short_description(self, obj):
        return obj.descriptions[:20] + '...' if len(obj.descriptions) > 20 else obj.descriptions
    
    preview_image.short_description = 'Фото'
    preview_icon.short_description = 'Выбор иконки'
    short_description.short_description = 'Описание'

    class Media:
        css = {
            'all': (
                'admin/css/custom.css',
                '/static/assets/css/flaticon.css',
            )
        }
        js = (
            'admin/js/vendor/jquery/jquery.js',
            'admin/js/jquery.init.js',
            'admin/js/core.js',
        )

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        class Media:
            js = ('js/icon_preview.js',)
        form.Media = Media
        return form

@admin.register(index_models.Reviews_Image)
class ReviewsImageAdmin(admin.ModelAdmin):
    list_display = ('preview_image',)
    readonly_fields = ('preview_image',)
    
    def preview_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 100px; border-radius: 5px; margin: 10px;"/>', 
                obj.image.url
            )
        return 'Нет изображения'
    
    preview_image.short_description = 'Фото'

    def has_add_permission(self, request):
        # Проверяем количество существующих записей
        if index_models.Reviews_Image.objects.count() >= 4:
            return False
        return True

    def get_queryset(self, request):
        # Сортируем записи по дате создания в обратном порядке
        return super().get_queryset(request).order_by('-id')

    class Media:
        css = {
            'all': ('admin/css/custom.css',)
        }
