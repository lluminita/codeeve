from django.conf.urls import url
from projects.views import (ProjectListView, ProjectCreate, ProjectDetailView,
                            ProjectUpdate)


urlpatterns = [

    url(r'^$',
        ProjectListView.as_view(),
        name='project_list'),
    url(r'^details/(?P<pk>\d+)/update/$',
        ProjectUpdate.as_view(),
        name='project_update'),
    url(r'^details/(?P<pk>\d+)/$',
        ProjectDetailView.as_view(),
        name='project_details'),
    url(r'^create/$',
        ProjectCreate.as_view(),
        name='project_create')
]
