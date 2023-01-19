from django import template

register = template.Library()

@register.inclusion_tag("course/partials/card.html")
def cardTag(course):
    context = {'course': course}
    return context
