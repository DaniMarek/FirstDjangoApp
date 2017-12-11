from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^new$', views.new),
	url(r'^create$', views.create),
	# the pattern above redirects
	url(r'^(?P<tracker_id>\d+)$', views.show),
	url(r'^(?P<tracker_id>\d+)/edit$', views.edit),
	url(r'^(?P<tracker_id>\d+)/delete$', views.delete)
	# the pattern above redirects
]
