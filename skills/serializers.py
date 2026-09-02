from rest_framework import serializers
from .models import Skill , SkillProof

class  SkillProofSerializer(serializers.ModelSerializer):
    certificate = serializers.SerializerMethodField()

    class Meta:
        model = SkillProof
        fields = ['id' , 'certificate' , 'project'] 

    def get_certificate(self , obj) :
        if obj.certificate:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.certificate.url)
            return None


class SkillSerializer(serializers.ModelSerializer):
    proofs = SkillProofSerializer(many = True , read_only = True)

    class Meta:
        model = Skill
        fields = ['id' , 'title' , 'icon' , 'proofs']
        