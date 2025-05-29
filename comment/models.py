from django.contrib.auth import get_user_model
from django.db import models
from note.models import CommonInfo

from note.models import Note

User = get_user_model()

class Comment(CommonInfo):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='comments')
    description = models.TextField()





