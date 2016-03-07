from django.conf.urls import url
from projects.views import ProjectListView, ProjectCreate


urlpatterns = [

    url(r'^$', ProjectListView.as_view(), name='project_list'),
    url(r'^create/$', ProjectCreate.as_view(), name='project_create'),
]
