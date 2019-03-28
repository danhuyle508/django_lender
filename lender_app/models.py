from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from django.contrib.auth.models import User


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=48)
    author = models.CharField(max_length=48)
    year = models.IntegerField()

    STATES =[
        ('available', 'Available'),
        ('checked-out', 'Checked-out')
    ]

    status = models.CharField(choices=STATES, default='checked-out', max_length=48)
    date_added = models.DateTimeField(default=timezone.now)
    last_borrowed = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f'<Book: { self.title } | Status: { self.status }>'

    def __str__(self):
        return f'{ self.title } | Status: { self.status }'