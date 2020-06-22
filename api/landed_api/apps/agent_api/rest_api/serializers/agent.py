from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.utils.encoding import smart_text

from landed_api.apps.agent_api.models.agent import Agent, Persona

class CreatableSlugRelatedField(serializers.SlugRelatedField):

    def to_internal_value(self, data):
        try:
            return self.get_queryset().get_or_create(**{self.slug_field: data})[0]
        except ObjectDoesNotExist:
            self.fail('does_not_exist', slug_name=self.slug_field, value=smart_text(data))
        except (TypeError, ValueError):
            self.fail('invalid')

class AgentSerializer(serializers.ModelSerializer):
    personas = CreatableSlugRelatedField(
        many=True,
        slug_field="name",
        queryset=Persona.objects.all()
    )

    class Meta:
        model = Agent
        fields = ("pk", "first_name", "last_name", "first_time_agent", "personas")

class PersonasSerializer(serializers.ModelSerializer):
    class Meta:
        model=Persona
        fields = ("name",)
    def to_representation(self, instance):
        return instance.name
