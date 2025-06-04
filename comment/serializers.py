from rest_framework import serializers

from comment.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = "__all__"


    def get_user(self, obj):
            return obj.user.email if obj.user else ""


    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data