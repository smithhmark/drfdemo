from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = patterns('snippets.views',
    url(r'^snippets/$', views.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', 'snippet_detail'),
)

urlpatterns = format_suffix_patterns(urlpatterns)
