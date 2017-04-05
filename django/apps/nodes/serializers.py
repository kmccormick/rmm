from rest_framework import serializers

from .models import Node, NodeIP


class NodeSerializer(serializers.ModelSerializer):
    ipaddrs = serializers.StringRelatedField(many=True)
    macaddrs = serializers.StringRelatedField(many=True)
    class Meta:
        model = Node
        fields = (
            'url',
            'hostname',
            'domain',
            'fqdn',
            'ipaddrs',
            'macaddrs',
        )
