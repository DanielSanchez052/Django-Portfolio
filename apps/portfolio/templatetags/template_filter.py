from django import template
from apps.portfolio.models import GeneralConfigModel
register = template.Library()


@register.filter
def get_dict(arr, key):
    for item in arr:
        if key in item:
            return item[key]
    return ''


@register.simple_tag(takes_context=False)
def content_by_section(section):
    return GeneralConfigModel.objects.get_content_dict(section)


@register.simple_tag(takes_context=False)
def content():
    return GeneralConfigModel.objects.get_content_dict()
