
from django.db import models

class MontageElementContainer(models.Model):
	title = models.CharField(max_length=3000)

class MontageElement(models.Model):
	video_file = models.FileField(upload_to='documents/%Y/%m/%d')
	container = models.ForeignKey(MontageElementContainer)