from .models import Conference
from modeltranslation.translator import TranslationOptions,register

@register(Conference)
class ConferenceTranslationOptions(TranslationOptions):
    fields = ('title', 'description')