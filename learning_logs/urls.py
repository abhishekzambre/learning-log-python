""" Define URL patterns for learning logs. """

from django.conf.urls import url

from . import views

urlpatterns = [
	# Home page
	url(r'^$', views.index, name='index'),

	# Show all topics.
	url(r'^topics/$', views.topics, name='topics'),

	# Details page for a single topic.
	url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]