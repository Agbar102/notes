from django.db import models
from note.models import CommonInfo, User

from note.models import Note


class Comment(CommonInfo):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='comments')
    description = models.TextField()





