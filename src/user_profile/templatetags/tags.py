from django import template
from django.http import HttpResponseNotFound
from django.urls import reverse

register = template.Library()

from user_profile.models import User


@register.simple_tag
def tag_user_id(pk):
    try:
        user = User.objects.get(id=pk)
    except User.DoesNotExist:
        return HttpResponseNotFound(f'User with id {pk} not found')
    return f'{user.email}'


# 8.template-tags - create template tag, that gets any model object, and renders a link of change view in admin interface
@register.simple_tag
def url_to_edit_object(obj):
    # url = reverse('admin:user_profile_user_change', args=[obj.id])
    url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
    # return f'<a href="{url}">Edit {obj.id}</a>'
    return url
