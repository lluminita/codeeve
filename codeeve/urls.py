from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView, RedirectView


urlpatterns = [
    # Examples:
    # url(r'^$', 'codeeve.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^$', TemplateView.as_view(template_name='codeeve/index.html'), name='home'),
    url(r'^projects/', include('projects.urls')),
    url(r'^accounts/profile/$', RedirectView.as_view(pattern_name='home')),
    url(r'^accounts/profile/$', RedirectView.as_view(pattern_name='home')),
]
