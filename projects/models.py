from django.db import models
from django.forms.models import ChoiceField
# Create your models here.
# Create the models projects


class Project(models.Model):
    # Project attributes
    title = models.CharField(max_length=200)
    description = models.TextField()
    max_members = models.IntegerField()
    difficulty = ChoiceField(choices=['beginner', 'intermediate', 'advanced'])
    # Project, user attributes
    owner = models.ForeignKey('auth.User', related_name='owns_project')
    participants = models.ManyToManyField('auth.User', related_name='participant_of_projects',
                                          blank=True)
    coach = models.ForeignKey('auth.User', related_name='coach_of_projects', null=True, blank=True)

    def __str__(self):
        return self.title
