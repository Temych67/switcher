from modeltranslation.translator import register, TranslationOptions
from testapp.models import InfoText

@register(InfoText)
class InfoTextTranslationOptions(TranslationOptions):
	fields = ('title', 'text')
