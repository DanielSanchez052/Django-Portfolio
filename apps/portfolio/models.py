from django.db import models
from django.urls import reverse

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

    # def get_absolute_url(self):
    #     return reverse("project_detail", kwargs={"slug": self.slug})


class GeneralConfigManager(models.Manager):
    def get_content_dict(self, filter=None):
        """
            return a dictionary for a content in general config where section is a key
            {
                section:[
                    {key:value},
                    {key:value},
                    {key:value},
                ]
            }
        """
        content_dict = dict()
        contents = self.all()

        if filter:
            contents = self.filter(section=filter)

        for content in contents:
            if content.section not in content_dict:
                content_dict[content.section] = list()

            content_dict[content.section].append(
                ({content.key: content.value}))
        return content_dict


class GeneralConfigModel(models.Model):
    key = models.CharField('key', max_length=255)
    value = models.TextField('value')
    section = models.CharField('section', max_length=150)
    objects = GeneralConfigManager()

    class Meta:
        verbose_name = 'Content'
        verbose_name_plural = 'Content'
        unique_together = ['key', 'section']

    def __str__(self) -> str:
        return f'{self.section}|{self.key}'
