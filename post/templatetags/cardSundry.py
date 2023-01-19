from django import template

register = template.Library()

@register.inclusion_tag("sundry/partials/card.html")
def cardTag(sundry):
    context = {'sundry': sundry}
    return context
