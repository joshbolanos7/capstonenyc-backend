from rest_framework import serializers
from .models import Landmark

class LandmarkSerializer(serializers.HyperlinkedModelSerializer):
    landmark_url = serializers.ModelSerializer.serializer_url_field(
        view_name='landmark_detail'
    )

    class Meta:
        model = Landmark
        fields = ('id', 'photo_url', 'landmark_url', 'name', 'description', 'address', 'type',)