from django.db import models

class InfoText(models.Model):
	title 		=	models.CharField(max_length=100, null=False)
	text 		=	models.TextField(max_length=2500, null=False)
		