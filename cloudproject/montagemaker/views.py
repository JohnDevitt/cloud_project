from django.http import HttpResponse
from django.template import RequestContext, loader

from montagemaker.models import MontageElementContainer
from montagemaker.models import MontageElement

from moviepy.editor import *

def create_montage(request):
	template = loader.get_template('montagemaker/create_montage.html')
	context = RequestContext(request, {
	})
	return HttpResponse(template.render(context))

def builder(request):

	montageElementContainer = MontageElementContainer(title = request.POST['title'])
	montageElementContainer.save()

	template = loader.get_template('montagemaker/builder.html')
	context = RequestContext(request, {
		'title': request.POST['title'],
	})
	return HttpResponse(template.render(context))

def montagify(request):
	for file in request.FILES.getlist('files'):
		montageElement = MontageElement(video_file = file, container = MontageElementContainer.objects.get(pk=1))
		montageElement.save()

	return HttpResponse("Done");