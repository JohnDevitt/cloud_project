from django.http import HttpResponse
from django.template import RequestContext, loader

from montagemaker.models import MontageElementContainer
from montagemaker.models import MontageElement

from montagemaker.forms import MontageCreateForm

from moviepy.editor import *

# Simple view to load a form that recieves the raw data for a montage
def create_montage(request):
	template = loader.get_template('montagemaker/create_montage.html')
	context = RequestContext(request, {
	})
	return HttpResponse(template.render(context))

#  This takes the data from the previous form, a loads an editor
def builder(request):

	# Create a montage with the supplied name
	montageElementContainer = MontageElementContainer(title = request.POST['title'])
	montageElementContainer.save()

	# contextDict for data to be passed to next view
	contextDict = {}
	contextDict['title']                   = request.POST['title']
	contextDict['montageElementContainer'] = montageElementContainer

	print("pre-test")

	for file in request.POST.getlist('files'):
		print("test")
		montageElement = MontageElement(video_file = file, container = montageElementContainer)
		montageElement.save()

	# Load the editor
	template = loader.get_template('montagemaker/builder.html')
	context = RequestContext(request, contextDict)
	return HttpResponse(template.render(context))

# Finished product
def montagify(request):


	print(request.POST['montageElementContainer'])
	