from django import template
register = template.Library()

SYMBOLS = {
    'дурак',
    'негодяй',
    'паразит',

}

@register.filter()
def censor(value):
    for item in SYMBOLS:
        value = value.replace(item[1:], '*' * len(item[1:]))
    return value