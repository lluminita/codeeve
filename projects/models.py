from django.db import models
from django.utils import timezone
# Create your models here.
# Create the models projects


class Project(models.Model):
    # Project attributes
    title = models.CharField(max_length=200)
    description = models.TextField()
    max_members = models.IntegerField()
    difficulty_choices = (
        ('beginner', 'beginner'),
        ('intermediate', 'intermediate'),
        ('advanced', 'advanced')
        )
    difficulty = models.CharField(max_length=15, choices=difficulty_choices)
    # Project, user attributes
    owner = models.ForeignKey('auth.User', related_name='owns_project')
    participants = models.ManyToManyField('auth.User', related_name='participant_of_projects',
                                          blank=True)
    coach = models.ForeignKey('auth.User', related_name='coach_of_projects', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/', blank=True, null = True)

    def __str__(self):
        return self.title
