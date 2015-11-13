from django.http import HttpResponse
from django.template import RequestContext, loader

def create_montage(request):
	template = loader.get_template('montagemaker/create_montage.html')
	context = RequestContext(request, {
	})
	return HttpResponse(template.render(context))

def builder(request):
	template = loader.get_template('montagemaker/builder.html')
	context = RequestContext(request, {
		'title': request.POST['title'],
	})
	return HttpResponse(template.render(context))