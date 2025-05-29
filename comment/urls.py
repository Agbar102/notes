from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', views.CommentViewSet, basename='comments')
urlpatterns = router.urls