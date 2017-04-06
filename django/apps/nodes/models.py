from django.db import models
from macaddress.fields import MACAddressField
from macaddress import default_dialect, format_mac

from apps.sites.models import Site

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
    hwtype = models.CharField(max_length=2, choices=HW_TYPES, default=PHYSICAL,
                             blank=True, null=True)
    ostype = models.CharField(max_length=3, choices=OS_TYPES, blank=True,
                              null=True)
    os = models.CharField(max_length=100, blank=True, null=True)
    nodetype = models.ForeignKey('NodeType', null=True,
                                 on_delete=models.CASCADE)
    default_site = models.ForeignKey(Site, related_name='default_site',
                                     null=True, on_delete=models.SET_NULL)
    sites = models.ManyToManyField(
        Site,
        through='NodeSite',
    )

    @property
    def fqdn(self):
        return '%s.%s' % (self.hostname, self.domain)

    def __str__(self):
        return self.fqdn

    def get_site(self, purpose):
        for site in self.sites.filter(nodesite__purpose=purpose):
            return site
        return self.default_site


class NodeIP(models.Model):
    node = models.ForeignKey(Node, related_name='ipaddrs',
                             on_delete=models.CASCADE)
    ipaddr = models.GenericIPAddressField()

    def __str__(self):
        return self.ipaddr


class NodeMAC(models.Model):
    node = models.ForeignKey(Node, related_name='macaddrs',
                             on_delete=models.CASCADE)
    macaddr = MACAddressField(integer=False)

    def __str__(self):
        return format_mac(self.macaddr, default_dialect())


class NodeType(models.Model):
    nodetype = models.CharField(max_length=50)

    def __str__(self):
        return self.nodetype


class NodeSite(models.Model):

    # "purposes" - why is this node related to this site?
    BILLING = 1
    PHYSICAL = 2
    REPORTING = 3
    PURPOSES = (
        (BILLING, 'billing'),
        (PHYSICAL, 'physical'),
        (REPORTING, 'reporting'),
    )

    node = models.ForeignKey(Node, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    purpose = models.PositiveSmallIntegerField(choices=PURPOSES)

    class Meta:
        # A node shouldn't be related to two different sites for the same reason
        unique_together = ('node', 'purpose')

    def __str__(self):
        return '{node} ({site} - {purpose})'.format(node=self.node, site=self.site,
                                                    purpose=self.get_purpose_display())
