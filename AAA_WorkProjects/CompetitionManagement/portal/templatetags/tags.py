from django import template
register = template.Library()


# enables to check for request to be set to current page
@register.simple_tag
def active(request, pattern):
    import re
    if re.search(pattern, request.path):
        return 'active'
    return ''