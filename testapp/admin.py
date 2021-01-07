from django.contrib import admin
from django import forms
from testapp.models import InfoText
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class TextAdminForm(forms.ModelForm):
	description_ru = forms.CharField(label='About', widget=CKEditorUploadingWidget())

	description_uk = forms.CharField(label='About', widget=CKEditorUploadingWidget())

	class Meta:
		model = InfoText
		fields = '__all__'

admin.site.register(InfoText)
