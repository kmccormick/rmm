from django.db import models
from macaddress.fields import MACAddressField


class Node(models.Model):

    # "Hardware" types
    PHYSICAL = 'hw'
    VIRTUAL = 'vm'
    SAAS = 'ss'
    HW_TYPES = (
        (PHYSICAL,'Physical'),
        (VIRTUAL,'Virtual'),
        (SAAS,'SaaS'),
    )

    # OS types
    WINDOWS = 'win'
    LINUX = 'lnx'
    UNIX = 'unx'
    MAC = 'mac'
    MOBILE = 'mob' # Android, Apple iOS, etc.
    EMBEDDED = 'emb' # Cisco IOS, FortiOS, etc.
    OTHER = 'oth'
    OS_TYPES = (
        (WINDOWS, 'Windows'),
        (LINUX, 'Linux'),
        (UNIX, 'Unix'),
        (MAC, 'Mac OS X / MacOS'),
        (MOBILE, 'Mobile Device OS'),
        (EMBEDDED, 'Embedded Device OS - switches, routers, etc.'),
        (OTHER, 'Other OS Type'),
    )

    hostname = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    fqdn = models.CharField(max_length=100)
    hwtype = models.CharField(max_length=2, choices=HW_TYPES, default=PHYSICAL,
                             blank=True, null=True)
    ostype = models.CharField(max_length=3, choices=OS_TYPES, blank=True,
                              null=True)
    os = models.CharField(max_length=100, blank=True, null=True)
    nodetype = models.ForeignKey('NodeType', null=True, on_delete=models.CASCADE)


class NodeIP(models.Model):
    node = models.ForeignKey(Node, on_delete=models.CASCADE)
    ipaddr = models.GenericIPAddressField()


class NodeMAC(models.Model):
    node = models.ForeignKey(Node, on_delete=models.CASCADE)
    macaddr = MACAddressField(integer=False)


class NodeType(models.Model):
    nodetype = models.CharField(max_length=50)
