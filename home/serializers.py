from rest_framework import serializers
from .models import Profile , SiteDocument

class ProfileSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model = Profile
        fields = ['id' , 'name' , 'role_title' , 'subtitle' , 'bio' , 'image' , 'is_available' , 'availability_label']

    def get_image(self , obj):
        if obj.image :
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None
        
class SiteDocumentSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField()

    class Meta:
        model = SiteDocument
        fields = ['id' , 'doc_type' , 'title' , 'file']

    def get_file(self , obj) :
        if obj.file:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.file.url)
            return obj.file.url
        return None