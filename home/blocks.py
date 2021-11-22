from django.conf.locale.ru.formats import DATE_INPUT_FORMATS
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.core.blocks import StructBlock, CharBlock, RichTextBlock, DateBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.blocks import ImageChooserBlock


class SlideshowBlock(StructBlock):
    """Класс для формирования слайда в слайд-шоу"""

    figure = ImageChooserBlock(label='Картинка')
    description = RichTextBlock(features=['link', 'bold'], label='Краткое описание', required=False)
    full_description = RichTextBlock(features=['link'], label='Описание', required=False)
    publication_date = DateBlock(label='Дата', required=False)

    class Meta:
        icon = 'view'
        label = 'Слайд'


class IntroTextBlock(StructBlock):
    """Класс для формирования статьи-вступления"""

    figure = ImageChooserBlock(label='Картинка')
    heading = CharBlock(label='Заголовок')
    sub_heading = RichTextBlock(label='Подзаголовок')
    text_intro = RichTextBlock(label='Вступительный текст')
    text_link = RichTextBlock(label='Текст ссылки')

    class Meta:
        icon = 'doc-full '
        label = 'Статья - intro'

