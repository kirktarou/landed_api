from django.urls import path
from .views import agent_view

urlpatterns = [
    path("agents/", agent_view.AgentListCreateAPIView.as_view(), name="api-agent-list"),
    path("agents/<uuid:pk>/", agent_view.AgentDetailsAPIView.as_view(), name="api-agent-details"),
]
