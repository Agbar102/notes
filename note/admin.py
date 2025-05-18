from django.contrib import admin
from note.models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display =  ["id", "title", "description", "user",]
    readonly_fields = ["created_at", "updated_at",]

admin.site.register(Note, NoteAdmin)
