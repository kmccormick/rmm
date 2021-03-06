from rest_framework import serializers

from .models import Site


class SiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Site
        fields = (
            'url',
            'name',
            'parent',
            'full_name',
        )
