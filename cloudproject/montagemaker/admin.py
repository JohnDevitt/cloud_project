from django.contrib import admin

from montagemaker.models import MontageElement, MontageElementContainer

admin.site.register(MontageElementContainer)
admin.site.register(MontageElement)