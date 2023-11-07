from rest_framework import viewsets
from rest_framework import permissions
from .models import Media
from .serializers import MediaSerializer

class MediaViewSet(viewsets.ModelViewSet):
    serializer_class = MediaSerializer
    permission_classes = [permissions.AllowAny]  # Could be [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Optionally filters the media by the 'tag' parameter in the query string.
        For example, /media/?tag=movie will filter media with the 'movie' tag.
        """
        queryset = Media.objects.all()
        tag = self.request.query_params.get('tag', None)
        if tag is not None:
            queryset = queryset.filter(tag__iexact=tag)
        return queryset
