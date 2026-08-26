from rest_framework import generics
from .models import SocialLink
from .serializers import SocialLinkSerializer

class SocialLinkListView(generics.ListAPIView):
    queryset = SocialLink.objects.all()
    serializer_class = SocialLinkSerializer