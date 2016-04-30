from django import template
from django.template import loader

from carousel import models

register = template.Library()

@register.simple_tag
def carousel(slug):
    carousel = models.Carousel.objects.get(slug=slug)

    carousel_template = loader.get_template("carousel/carousel.html")
    return carousel_template.render({
        'carousel': carousel
    })
