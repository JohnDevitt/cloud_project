from django.conf.urls import patterns, url

urlpatterns = patterns('montagemaker.views',
    url(r'^create_montage/$', 'create_montage', name='create_montage'),
    url(r'^builder/$', 'builder', name='builder'),
)