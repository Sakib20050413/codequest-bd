import markdown as md_lib
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name="render_md")
def render_md(text):
    if not text:
        return ""
    try:
        html = md_lib.markdown(
            text,
            extensions=["fenced_code", "tables", "codehilite", "nl2br"],
        )
        return mark_safe(html)
    except Exception:
        return mark_safe(text)
