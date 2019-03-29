from django.utils import timezone
from django import template

register = template.Library()

@register.filter
def get_date_string(value):
    now_aware = timezone.now()
    delta = value - now_aware

    if delta.days == 0:
        return "today"
    if delta.days < 1:
        return f'{delta.days} Day(s) ago'
    elif delta.days == 1:
        return'tomorrow'
    elif delta.days > 1:
        return f'In {delta.days} day(s).'
