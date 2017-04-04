from django.contrib import admin
from .models import *


class InlineNodeIP(admin.TabularInline):
    model = NodeIP


class InlineNodeMAC(admin.TabularInline):
    model = NodeMAC


class NodeAdmin(admin.ModelAdmin):
    inlines = [
        InlineNodeIP,
        InlineNodeMAC,
    ]

admin.site.register(Node, NodeAdmin)
admin.site.register(NodeType)
