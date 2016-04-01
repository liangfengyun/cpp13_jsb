from django.conf.urls import patterns, include, url
from homeapp import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cpp13_jsb_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^index/$', views.index, name="index"),
    url(r'^add/$', views.add, name="add"),
    url(r'^delete/$', views.delete, name="delete"),
)
