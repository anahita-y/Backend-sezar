from rest_framework import serializers
from .models import Profile , SiteDocument

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

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