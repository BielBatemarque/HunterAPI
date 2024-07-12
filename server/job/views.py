from rest_framework import viewsets
from job.models import Job, Portal
from job.serializers import JobSerializer, PortalSerializer
# Create your views here.
class JobViewSets(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class PortalViewSets(viewsets.ModelViewSet):
    queryset = Portal.objects.all()
    serializer_class = PortalSerializer