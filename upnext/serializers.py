from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import Media

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ['id', 'title', 'release_date', 'image_link', 'priority', 'tag']
