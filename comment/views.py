from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django_filters import rest_framework as filters

from comment.models import Comment
from comment.paginations import LargeResultsSetPagination
from comment.serializers import CommentSerializer
from comment.filters import CommentFilter


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    # filterset_fields = ('description',)
    filterset_class = CommentFilter
    pagination_class = LargeResultsSetPagination
    permission_classes = []

    description = openapi.Parameter('description', openapi.IN_QUERY,
                                    description="Передаем description",type=openapi.TYPE_STRING)

    created_at = openapi.Parameter('created_at', openapi.IN_QUERY,
                                   description="Передаем время создания",type=openapi.TYPE_NUMBER)

    user = openapi.Parameter('user', openapi.IN_QUERY,
                                   description="Передаем user", type=openapi.TYPE_INTEGER)


    @swagger_auto_schema(manual_parameters=[description, created_at, user  ])
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # def get_queryset(self):
    #     search = self.request.query_params.get("search")
    #     start_date = self.request.query_params.get("start_date")
    #     end_date = self.request.query_params.get("end_date")
    #     comments = Comment.objects.all().order_by('-created_at')
    #     if search:
    #         comments = Comment.objects.filter(description__icontains=search).order_by('created_at')
    #
    #     if start_date and not end_date:
    #         comments = Comment.objects.filter(created_at__gte=start_date)
    #
    #     if end_date and not start_date:
    #         comments = Comment.objects.filter(created_at__lte=end_date)
    #
    #     if start_date and end_date:
    #         comments = Comment.objects.filter(created_at__gte=start_date, created_at__lte=end_date)
    #     return comments


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # @action(detail=False, methods=["get"], url_path='l')
    # def search_comments(self, request):
    #     search = request.query_params.get("search")
    #     comments = self.get_queryset().order_by('-created_at')
    #     if search:
    #         comments = comments.filter(description__icontains=search)
    #     serializer = self.get_serializer(comments, many=True)
    #     return Response(serializer.data)
