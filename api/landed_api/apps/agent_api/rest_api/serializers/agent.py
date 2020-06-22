from rest_framework import serializers

from landed_api.apps.agent_api.models.agent import Agent


class AgentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Agent
        fields = ("pk", "first_name", "last_name", "first_time_agent")