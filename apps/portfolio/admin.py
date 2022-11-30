from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import ProjectModel, GeneralConfigModel
# Register your models here.


class ProjectModelResource(resources.ModelResource):
    class Meta:
        model = ProjectModel


@admin.register(ProjectModel)
class ProjectModelAdmin(ImportExportModelAdmin):
    resource_classes = [ProjectModelResource]
    list_display = ['title', 'slug', 'image', 'status', 'is_active']


class GeneralConfigResource(resources.ModelResource):
    class Meta:
        model = GeneralConfigModel


@admin.register(GeneralConfigModel)
class ProjectModelAdmin(ImportExportModelAdmin):
    resource_classes = [GeneralConfigResource]
    list_display = ['key', 'value', 'section']
    list_filter = ['section']
