from django.db import models
from wagtail.core.models import Page


class CatalogPage(Page):
    """Страница для выведения информации о продукции"""

    max_count = 1
    parent_page_types = ['home.HomePage']
