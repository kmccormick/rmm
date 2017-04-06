from . import views

routes = [
    (r'nodes', views.NodeViewSet),
    (r'nodesites', views.NodeSiteViewSet),
]
