from django.contrib import admin
from .models import ProjectModel, GeneralConfigModel
# Register your models here.


@admin.register(ProjectModel)
class ProjectModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'image', 'status', 'is_active']


@admin.register(GeneralConfigModel)
class ProjectModelAdmin(admin.ModelAdmin):
    list_display = ['key', 'value', 'section']
