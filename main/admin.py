# pylint: disable=no-member
from django.contrib import admin
from django import forms
from django.shortcuts import render, redirect
from django.urls import path
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.utils.html import format_html
from django.urls import reverse

from main.models import Routes
import openpyxl
from datetime import datetime

class ImportExcelForm(forms.Form):
    excel_file = forms.FileField(label='Файл Excel (.xlsx)')
    
    def clean_excel_file(self):
        file = self.cleaned_data['excel_file']
        if not file.name.endswith('.xlsx'):
            raise forms.ValidationError("Поддерживаются только файлы .xlsx")
        return file

@admin.register(Routes)
class RoutesAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'distance', 'duration', 'transportation_method', 'cost', 'admin_image')
    list_filter = ('level', 'transportation_method')
    search_fields = ('name', 'organizing_agency')
    list_per_page = 20
    
    # Кастомный шаблон для списка маршрутов
    change_list_template = 'admin/routes_change_list.html'
    
    # Поля для формы редактирования
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'level', 'duration', 'distance', 'transportation_method', 'cost')
        }),
        ('Дополнительная информация', {
            'fields': ('event_date', 'organizing_agency', 'contact_info', 'skill_name'),
            'classes': ('collapse',)
        }),
        ('Файлы и ссылки', {
            'fields': ('route_passport', 'map_link', 'image'),
            'classes': ('collapse',)
        }),
    )
    
    # Добавляем кнопку импорта в интерфейс
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('import-excel/', self.admin_site.admin_view(self.import_excel), name='import_excel'),
        ]
        return custom_urls + urls
    
    # Логика импорта из Excel
    def import_excel(self, request):
        if request.method == 'POST':
            form = ImportExcelForm(request.POST, request.FILES)
            if form.is_valid():
                try:
                    wb = openpyxl.load_workbook(form.cleaned_data['excel_file'])
                    ws = wb.active
                    
                    created_count = 0
                    for row in ws.iter_rows(min_row=2, values_only=True):
                        if not row[0]:  # Пропускаем пустые строки
                            continue
                            
                        Routes.objects.create(
                            name=row[0] or '',
                            level=row[1] or 0,
                            duration=row[2] or 0,
                            distance=row[3] or 0,
                            transportation_method=row[4] or '',
                            cost=row[5] or 0,
                            event_date=row[6] if row[6] else None,
                            organizing_agency=row[7] or None,
                            contact_info=row[8] or None,
                            skill_name=row[9] or None,
                            route_passport=row[10] or None,
                            map_link=row[11] or None,
                        )
                        created_count += 1
                    
                    messages.success(
                        request,
                        f'Успешно импортировано {created_count} маршрутов'
                    )
                    return redirect('..')
                
                except Exception as e:
                    messages.error(
                        request,
                        f'Ошибка при импорте: {str(e)}'
                    )
        else:
            form = ImportExcelForm()
        
        context = {
            'form': form,
            'opts': self.model._meta,
            'title': 'Импорт маршрутов из Excel',
            **self.admin_site.each_context(request),
        }
        return render(request, 'admin/import_excel.html', context)
    
    # Показываем миниатюру изображения в списке
    def admin_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 50px; max-width: 50px;" />',
                obj.image.url
            )
        return "-"
    admin_image.short_description = 'Изображение'
