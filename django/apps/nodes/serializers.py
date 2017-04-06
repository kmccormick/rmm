from rest_framework import serializers

from .models import Node, NodeSite
from .fields import NamedChoiceField


class NodeSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = NodeSite
        fields = (
            'url',
            'purpose',
            'site',
        )
    purpose = NamedChoiceField(choices=NodeSite.PURPOSES)


class NodeSerializer(serializers.ModelSerializer):
    ipaddrs = serializers.StringRelatedField(many=True)
    macaddrs = serializers.StringRelatedField(many=True)
    # source=nodesite_set is required here to get access to the NodeSite
    # 'through' model; otherwise this will try to serialize a Site object
    # which has no purpose field
    sites = NodeSiteSerializer(source='nodesite_set', many=True)

    class Meta:
        model = Node
        fields = (
            'url',
            'hostname',
            'domain',
            'fqdn',
            'default_site',
            'sites',
            'ipaddrs',
            'macaddrs',
        )
