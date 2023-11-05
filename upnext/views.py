from .models import Media
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import MediaSerializer


class MediaViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Media.objects.all()
    # The serializer class for serializing output
    serializer_class = MediaSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] #Coule be [permissions.IsAuthenticated]