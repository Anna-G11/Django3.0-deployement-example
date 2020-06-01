from django import template

register = template.Library()
@register.filter('cut')
def cut(value,arg):

    return valur.replace(arg,'')

# register.filter('cut',cut)
