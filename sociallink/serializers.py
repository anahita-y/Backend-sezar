from rest_framework import serializers
from .models import SocialLink

class SocialLinkSerializer(serializers.ModelSerializer):
    class  Meta:
        model = SocialLink
        fields = ['id' , 'platform' , 'icon' , 'url_or_value' , 'label' , 'map_link']
