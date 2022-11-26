from django.db import models

# Create your models here.


class ProjectModel(models.Model):
    STATUS_CHOICE = (
        ('CP', 'COMPLETO'),
        ('PA', 'PAUSADO'),
        ('IN', 'INCOMPLETO'),
        ('IP', 'EN PROCESO')
    )
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='project/images')
    github = models.URLField(blank=True)
    url = models.URLField(blank=True)
    status = models.CharField(
        max_length=2, choices=STATUS_CHOICE, default='IP')
    is_active = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True, auto_now=False)
    updated_at = models.DateField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self) -> str:
        return self.slug


class GeneralConfigModel(models.Model):
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=500)
    section = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'General Config'
        verbose_name_plural = 'General Config'

    def __str__(self) -> str:
        return f'{self.section}|{self.key}'
