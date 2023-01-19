from django import template

register = template.Library()

@register.inclusion_tag("post/partials/comment.html")
def commentTag(comment, reply, form, request):
    context = {'comment': comment, 'reply': reply, 'form': form, 'request': request}
    return context
