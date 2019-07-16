from django.utils.translation import gettext_lazy as _

from wagtail.admin.edit_handlers import StreamFieldPanel, TabbedInterface, ObjectList
from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.utils.decorators import cached_classmethod


class BasicPage(Page):
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body_cs'),
    ]

    content_panels_en = [
        StreamFieldPanel('body_en'),
    ]

    # https://stackoverflow.com/questions/41668167/what-is-the-correct-way-to-extend-wagtail-abstract-models-with-extra-fields
    # https://stackoverflow.com/questions/1817183/using-super-with-a-class-method
    # https://github.com/wagtail/wagtail/blob/master/wagtail/admin/edit_handlers.py
    @cached_classmethod
    def get_edit_handler(cls):
        edit_handler = super().get_edit_handler()
        tabs = edit_handler.clone_kwargs()['children']
        tabs.insert(1, ObjectList(cls.content_panels_en, heading='En'))
        edit_handler = TabbedInterface(tabs, base_form_class=cls.base_form_class)
        return edit_handler.bind_to(model=cls)
