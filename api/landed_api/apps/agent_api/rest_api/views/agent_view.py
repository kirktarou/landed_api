from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView

from landed_api.apps.agent_api.models.agent import Agent, Persona, Region
from landed_api.apps.agent_api.rest_api.serializers.agent import AgentSerializer, PersonasSerializer, RegionSerializer


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

class PersonaListAPIView(ListAPIView):
    """
    API view to retrieve agent personas
    """
    serializer_class = PersonasSerializer
    queryset = Persona.objects.all()

class RegionListAPIView(ListAPIView):
    """
    API view to retrieve agent personas
    """
    serializer_class = RegionSerializer
    queryset = Region.objects.all()