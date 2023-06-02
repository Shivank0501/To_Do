from django.db import models


class Task(models.Model):
    STATUS_CHOICES = (
        ('todo', 'Open'),
        ('in_progress', 'Working'),
        ('completed', 'Done'),
        ('overdue', 'Overdue')
    )

    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(max_length=1000, blank=False, null=False)
    due_date = models.DateField( blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo', blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
