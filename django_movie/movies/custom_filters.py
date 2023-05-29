from django import template
from views import get_embedded_youtube_url  # Import hàm get_embedded_youtube_url từ views.py

register = template.Library()

@register.filter(name='get_embedded_youtube_url')
def get_embedded_youtube_url(value):
    return get_embedded_youtube_url(value)