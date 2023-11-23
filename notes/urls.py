from django.urls import path
from . import views

urlpatterns = [
    path("list-notes/", views.ListNoteView.as_view(), name="list-view"),
    path("add-notes/", views.AddNoteView.as_view(), name="add-view"),
    path(
        "retrieve-update-notes/<int:note_pk>/",
        views.RetrieveUpdateNoteView.as_view(),
        name="retrieve-update-view",
    ),
    path(
        "delete-notes/<int:note_pk>/",
        views.DeleteNoteView.as_view(),
        name="delete-view",
    ),
    path(
        "summary-note/<int:note_pk>/",
        views.SummaryAiView.as_view(),
        name="summary-view",
    ),
]
