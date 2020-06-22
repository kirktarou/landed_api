from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from landed_api.apps.agent_api.models.agent import Agent
from landed_api.apps.agent_api.rest_api.serializers.agent import AgentSerializer


class AgentListCreateAPIView(ListCreateAPIView):
    """
    API view to retrieve list of posts or create new
    """

    serializer_class = AgentSerializer
    queryset = Agent.objects.active()


class AgentDetailsAPIView(RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete post
    """

    serializer_class = AgentSerializer
    queryset = Agent.objects.active()