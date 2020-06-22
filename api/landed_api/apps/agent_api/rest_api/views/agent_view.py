from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView

from landed_api.apps.agent_api.models.agent import Agent, Persona
from landed_api.apps.agent_api.rest_api.serializers.agent import AgentSerializer, PersonasSerializer


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