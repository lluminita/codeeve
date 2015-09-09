from django.conf.urls import url

from projects.views import ProjectListView


urlpatterns = [

    url(r'^$', ProjectListView.as_view(), name='list_projects')
]
