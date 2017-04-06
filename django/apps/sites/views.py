from rest_framework import viewsets
from . import models, serializers


class SiteViewSet(viewsets.ModelViewSet):
    queryset = models.Site.objects.all()
    serializer_class = serializers.SiteSerializer
