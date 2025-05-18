from django.db import models
from note.models import CommonInfo

from note.models import Note


class Comment(CommonInfo):
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='comments')
    description = models.TextField()





