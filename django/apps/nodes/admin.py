from django.contrib import admin
from .models import *


class InlineNodeIP(admin.TabularInline):
    model = NodeIP


class InlineNodeMAC(admin.TabularInline):
    model = NodeMAC


class InlineNodeSite(admin.TabularInline):
    model = NodeSite


class NodeAdmin(admin.ModelAdmin):
    inlines = [
        InlineNodeSite,
        InlineNodeIP,
        InlineNodeMAC,
    ]

admin.site.register(Node, NodeAdmin)
admin.site.register(NodeType)
