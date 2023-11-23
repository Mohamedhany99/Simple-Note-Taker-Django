from rest_framework import generics
from .serializers import NoteSerializer
from .models import Note

# Create your views here.


class ListNoteView(generics.ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class AddNoteView(generics.CreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class UpdateNoteView(generics.RetrieveUpdateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)


class DeleteNoteView(generics.DestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
