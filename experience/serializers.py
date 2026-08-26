from rest_framework import serializers
from .models import Experience

class ExperienceSerializer(serializers.ModelSerializer):
    status_display = serializers.CharField(source = 'get_status_display', read_only = True)
    image =  serializers.SerializerMethodField()

    class Meta:
        model = Experience
        fields = ['id' , 'year' , 'title' , 'short_description' , 'image' , 'status' , 'status_display']

        def get_image(self, obj):
            if obj.image :
                request= self.context.get('request') 
                if request :
                    return request.build_absolute_uri(obj.image.url)
                return obj.image.url
            return None