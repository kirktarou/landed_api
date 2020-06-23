from django_filters import rest_framework as filters
from django_filters import OrderingFilter
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView

from landed_api.apps.agent_api.models.agent import Agent, Persona, Region
from landed_api.apps.agent_api.rest_api.serializers.agent import AgentSerializer, PersonasSerializer, RegionSerializer


class AgentFilter(filters.FilterSet):
    region = filters.ModelMultipleChoiceFilter(field_name='region__name', to_field_name='name', queryset=Region.objects.all())
    first_name = filters.CharFilter(field_name='first_name', lookup_expr='icontains')
    last_name = filters.CharFilter(field_name='last_name', lookup_expr='icontains')
    persona = filters.ModelMultipleChoiceFilter(
        field_name='persona__name', 
        to_field_name='name',
        queryset=Persona.objects.all(),
        )
    class Meta:
        model = Agent
        fields = ['first_name', 'last_name', 'first_time_agent', 'region', 'persona']

class AgentListCreateAPIView(ListCreateAPIView):
    """
    API view to retrieve list of posts or create new
    """

    serializer_class = AgentSerializer
    queryset = Agent.objects.active()
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = AgentFilter


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