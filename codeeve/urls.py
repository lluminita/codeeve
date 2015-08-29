from django.conf.urls import include, url
from django.contrib import admin

from . import views


urlpatterns = [
    # Examples:
    # url(r'^$', 'codeeve.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home, name='home')
]
