from .models import BasicPage
from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register


@register(BasicPage)
class BasicPageTR(TranslationOptions):
    fields = (
        'body',
    )
