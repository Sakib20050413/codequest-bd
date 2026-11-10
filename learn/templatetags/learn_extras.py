from django import template
from django.utils.safestring import mark_safe

try:
    import markdown as md_lib
except ImportError:
    md_lib = None

register = template.Library()

@register.filter(name="render_md")
def render_md(text):
    if not text:
        return ""
    if md_lib:
        try:
            html = md_lib.markdown(
                text,
                extensions=["fenced_code", "tables", "codehilite", "nl2br"],
            )
            return mark_safe(html)
        except Exception:
            pass
    return mark_safe(text)
