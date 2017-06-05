from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
	url(r'^$', view=views.index, name='index'),
	url(r'^(?P<slug>[-\w\d]+)/$', view=views.image_post, name='image_post'),
	
]
