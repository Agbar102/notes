from django_filters import rest_framework as filters
from comment.models import Comment


class CommentFilter(filters.FilterSet):
    description = filters.CharFilter(lookup_expr='icontains')
    created_at = filters.DateFromToRangeFilter()

    class Meta:
        model = Comment
        fields = ['description', 'created_at', 'user']