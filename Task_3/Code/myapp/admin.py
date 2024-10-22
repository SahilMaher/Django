from django.contrib import admin
from django.http import HttpResponse
from .views import export_data
from django.urls import path
from .models import PersonData
# Register your models here.
@admin.register(PersonData)
class PersonAdminModel(admin.ModelAdmin):
    actions=['export_as_csv']
    def export_as_csv(slf,request,queryset):
        return HttpResponse('/export/')
    export_as_csv.short_description="Export Data as Csv"
    def get_urls(self):
        urls= super().get_urls()
        custom_urls=[
            path('export/',self.admin_site.admin_view(export_data),name='export_data')
        ]
        return custom_urls+urls