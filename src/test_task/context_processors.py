from django.conf import settings


# 4. Create template context processor that add django.conf.settings to context.
def settings_content(request):
    settings_list = {}
    for attr in dir(settings):
        value = getattr(settings, attr)
        settings_list[attr] = value

    return settings_list
