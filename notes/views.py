from rest_framework import generics
from .serializers import NoteSerializer
from .models import Note
from rest_framework.response import Response
from rest_framework import status, exceptions

# Create your views here.


class ListNoteView(generics.ListAPIView):
    """List all the notes API"""

    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class AddNoteView(generics.CreateAPIView):
    """Add new Note"""

    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def post(self, request, *args, **kwargs):
        mutable_dict = request.data.copy()
        print(mutable_dict)
        return super().create(request, *args, **kwargs)


class RetrieveUpdateNoteView(generics.RetrieveUpdateAPIView):
    """Retrieve Update API"""

    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def patch(self, request, note_pk):
        try:
            note = Note.objects.get(pk=note_pk)
            serializer = self.get_serializer(
                instance=note, data=request.data, partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(
                    data=serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE
                )
        except Note.DoesNotExist:
            raise exceptions.NotFound("Cannot Find Note")
        except Exception as e:
            print(e)
            raise exceptions.NotAcceptable("Something Went Wrong")

    def get(self, request, note_pk):
        try:
            note = Note.objects.get(pk=note_pk)
            serializer = self.serializer_class(instance=note)
            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)

        except Note.DoesNotExist:
            raise exceptions.NotFound("Cannot Find Note")

        except Exception as e:
            print(e)
            raise exceptions.NotAcceptable("Something Went Wrong")


class DeleteNoteView(generics.DestroyAPIView):
    """Delete Note API"""

    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def destroy(self, request, note_pk):
        try:
            note = Note.objects.get(id=note_pk)
            note.delete()
            return Response(data="Note Deleted Successfuly", status=status.HTTP_200_OK)
        except Note.DoesNotExist:
            raise exceptions.NotFound("Cannot Find Note")
        except Exception as e:
            print(e)
            raise exceptions.NotAcceptable("Something Went Wrong")
