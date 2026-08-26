from rest_framework import generics
from .models import Technology , Project
from .serializers import TechnologySerializer, ProjectSerializer

class TechnologyListView(generics.ListAPIView):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer


class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetailView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class  = ProjectSerializer