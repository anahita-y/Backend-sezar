from rest_framework import generics
from .models import Profile , SiteDocument
from .serializers import ProfileSerializer , SiteDocumentSerializer

class ProfileView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer

    def get_object(self):
        return Profile.objects.first()

class SiteDocumentListView(generics.ListAPIView):
    queryset = SiteDocument.objects.all()
    serializer_class = SiteDocumentSerializer