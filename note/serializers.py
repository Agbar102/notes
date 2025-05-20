from symtable import Class

from rest_framework import serializers

import comment
from comment.models import Comment
from note.models import Note


class NoteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"
        extra_kwargs = {
            'user': {"required": False},
        }


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()


    class Meta:
         model = Comment
         fields = ['description', 'created_at', 'user']

    def get_user(self, obj):
        return obj.user.email if obj.user else ""


    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data


class NotesSerializer(CommentSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Note
        fields = [ 'id', 'created_at', 'updated_at', 'delete_at',
            'title', 'is_private', 'description', 'user', 'comments']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['delete_at'] = instance.delete_at if instance.delete_at else None
        return data






