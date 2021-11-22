from django.db import models
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core import blocks
from wagtail.core.blocks import RichTextBlock
from wagtail.core.fields import StreamField
from wagtail.core.models import Page

from home.blocks import SlideshowBlock, IntroTextBlock


class HomePage(Page):

    subpage_types = ['about.AboutPage']

    body = StreamField(
        [
            ('heading', RichTextBlock(
                label='Заголовок',
                help_text='Введите название заголовка')),
            ('slideshow', blocks.ListBlock(SlideshowBlock(), label='Слайды')),
            ('article_intro', IntroTextBlock()),


        ],
        # block_counts={
        #     'events_news': {'max_num': 1},
        #     'products': {'max_num': 1},
        # },
        blank=True,
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
