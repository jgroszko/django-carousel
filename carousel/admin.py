from django.contrib import admin

from carousel import models

class CarouselSlideAdmin(admin.StackedInline):
    model = models.CarouselSlide

class CarouselAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']

    inlines = [
        CarouselSlideAdmin,
    ]

admin.site.register(models.Carousel, CarouselAdmin)
