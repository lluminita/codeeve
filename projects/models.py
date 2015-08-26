from django.db import models
from django.forms.models import ChoiceField
# Create your models here.
# Create the models projects


class Project(models.Model):
    title = models.CharField(max_length=200)
    owner = models.ForeignKey('auth.User', related_name='owns_project')
    description = models.TextField()
    max_members = models.IntegerField()
    participants = models.ManyToManyField('auth.User', related_name='participant_of_projects')
    difficulty = ChoiceField(choices=['beginner', 'intermediate', 'advanced'])
