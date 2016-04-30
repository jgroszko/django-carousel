from django.db import models
from django.utils.translation import ugettext_lazy as _

from mezzanine.core.models import Orderable

class Carousel(models.Model):
    name = models.CharField(max_length=255)

    slug = models.SlugField()

    indicators = models.BooleanField()

    class Meta:
        verbose_name = _("Carousel")
        verbose_name_plural = _("Carousels")

    def __str__(self):
        return self.name

class CarouselSlide(Orderable):
    name = models.CharField(max_length=255)

    image_url = models.CharField(max_length=512)

    link_url = models.CharField(max_length=255, blank=True)

    description = models.TextField(blank=True)

    carousel = models.ForeignKey(Carousel, related_name="slides")

    class Meta:
        verbose_name = _("Slide")
        verbose_name_plural = _("Slides")

        ordering = ["_order",]

    def __str__(self):
        return self.name
