from rest_framework import viewsets
from . import models, serializers


class NodeSiteViewSet(viewsets.ModelViewSet):
    queryset = models.NodeSite.objects.all()
    serializer_class = serializers.NodeSiteSerializer


class NodeViewSet(viewsets.ModelViewSet):
    queryset = models.Node.objects.all()
    serializer_class = serializers.NodeSerializer
