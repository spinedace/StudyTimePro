from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
from django.utils import timezone

# Create your models here.


class Task(models.Model):
    SET_OF_CHOICES = (
        ('choice1', 'Baja'),
        ('choice2', 'Media'),
        ('choice3', 'Alta'),
        ('choice4', 'Sin prioridad'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks", null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateField(auto_now=False)
    due_date = models.DateField(null=True, blank=True)
    priority = models.CharField(choices=SET_OF_CHOICES, max_length=10)

    def save(self, *args, **kwargs):
        if not self.due_date:
            self.due_date = self.created + timedelta(days=1)
        super(Task, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']

class Calendar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(default='Untitled Calendar', max_length=200, null=False)
    description = models.TextField(blank=True)
    start_date = models.DateField(default=timezone.now, null=False)
    end_date = models.DateField()
    events = models.ManyToManyField(Task, blank=True)

    def __str__(self):
        return self.title
