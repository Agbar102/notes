from django.urls import path

from . import views

urlpatterns = [
    path("", views.NoteApiView.as_view()),
    path("create/", views.NoteCreateAPIView.as_view()),
    path("<int:pk>/", views.NoteDetailAPIView.as_view()),
]


