from rest_framework import serializers
from .models import Technology , Project , ProjectDetail

class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ['id' , 'name']

class ProjectDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectDetail
        fields = ['challenge' , 'solution' , 'result' , 'demo_link']

class ProjectSerializer(serializers.ModelSerializer):
    technologies = TechnologySerializer(many = True, read_only = True)
    detail = ProjectDetailSerializer(read_only = True)
    image = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ['id' , 'title' , 'short_description' , 'technologies' , 'image' , 'detail']

def get_image(self , obj):
    if obj.image:
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(obj.image.url)
        return obj.image.url
    return None