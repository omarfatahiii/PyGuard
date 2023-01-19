from django import template

register = template.Library()

@register.inclusion_tag("post/partials/card.html")
def cardTag(post):
    context = {'post': post}
    return context
