from django.db import models
from django.db.models import CASCADE

from users.models import CustomUser


class Note(models.Model):
    title = models.CharField(max_length=255)
    is_private = models.BooleanField(default=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='notes')

    def __str__(self):
        return self.title

