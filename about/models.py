from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import StreamFieldPanel, MultiFieldPanel, FieldPanel, InlinePanel, FieldRowPanel
from wagtail.contrib.forms.models import AbstractFormField, AbstractEmailForm
from wagtail.core.blocks import RichTextBlock
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core.models import Page


class AboutChildPage(Page):
    """Дочерняя страница от AboutPage"""

    subpage_types = []
    parent_page_types = ['about.AboutPage']

    body = StreamField(
        [
            ('heading_general', RichTextBlock(
                features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'link', 'bold', 'italic'],
                label='Заголовок',
                help_text='Введите название заголовка')),
            ('article', RichTextBlock(label='Статья')),
            ('article_two_columns', RichTextBlock(label='Статья на двух колонках')),

        ],
        blank=True,
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]


class FormField(AbstractFormField):
    """Поле для отправки формы"""
    form_field = ParentalKey(
        'AboutPage',
        on_delete=models.CASCADE,
        related_name='form_fields',
    )


class AboutPage(AbstractEmailForm):
    """Страница для выведения информации о компании"""

    max_count = 1
    parent_page_types = ['home.HomePage']
    subpage_types = ['about.AboutChildPage']

    body = StreamField(
        [
            ('heading_general', RichTextBlock(
                features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'link', 'bold', 'italic'],
                label='Заголовок',
                help_text='Введите название заголовка')),
            ('article', RichTextBlock(label='Статья')),
            ('article_two_columns', RichTextBlock(label='Статья на двух колонках')),


        ],
        blank=True,
    )

    intro = RichTextField(
        blank=True,
        verbose_name='Предварительный текст',
    )
    thank_you_text = RichTextField(
        blank=True,
        verbose_name='Текст после отправки формы',
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            StreamFieldPanel('body')],
            heading='Информация и статьи о компании'),
        FieldPanel('intro'),
        InlinePanel('form_fields', label='Поля формы для отправки вопроса'),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname='col6'),
                FieldPanel('to_address', classname='col6'),
            ]),
            FieldPanel('subject'),
        ], heading='Настройки электронной почты'),
    ]
