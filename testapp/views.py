from django.shortcuts import render
from testapp.models import InfoText

def main_translater(request):
	text = InfoText.objects.all()
	context={'text':text}
	return render(request, 'main_translater.html', context)