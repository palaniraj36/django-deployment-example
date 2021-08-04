from django import template

register = template.Library()
@register.filter(name="cuti")
def cuti(value,arg):
    """""
     this cuts all value from the string
    """""
    return value.replace(arg,'')

# register.filter('cuti',cuti)
