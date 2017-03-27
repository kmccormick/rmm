from rest_framework import serializers

from .models import Node, NodeIP


class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = (
            'url',
            'hostname',
            'domain',
            'fqdn',
            'ipaddrs',
        )
    ipaddrs = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

class NodeIPSerializer(serializers.ModelSerializer):
    class Meta:
        model = NodeIP
        fields = (
            'url',
            'ipaddr',
        )
