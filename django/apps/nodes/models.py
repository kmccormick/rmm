from django.db import models


class Node(models.Model):
    hostname = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    fqdn = models.CharField(max_length=100)
    ipaddrs = models.ForeignKey('NodeIP', blank=True, null=True,
                                on_delete=models.CASCADE)


class NodeIP(models.Model):
    ipaddr = models.GenericIPAddressField()
