from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet


@register_snippet
class Header(models.Model):
    """Класс для формирования фрагмента хедера сайта"""

    panels = []

    class Meta:
        verbose_name = 'Хедер'
        verbose_name_plural = 'Хедеры'

    def __str__(self):
        return 'Хедер'


@register_snippet
class Footer(models.Model):
    """Класс для формирования фрагмента футера сайта"""

    panels = []

    class Meta:
        verbose_name = 'Футер'
        verbose_name_plural = 'Футеры'

    def __str__(self):
        return 'Футер'
