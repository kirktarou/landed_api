from django.test import TestCase

from landed_api.apps.agent_api.models.agent import Agent, Persona

class AgentTestCase(TestCase):
    def test_agent(self):
        self.assertEquals(Agent.objects.count(), 0)
        agent = Agent.objects.create(first_name="Kirk", last_name="Tarou", first_time_agent=True)
        self.assertEquals(Agent.objects.count(), 1)
        active_agents = Agent.objects.active()
        self.assertEquals(active_agents.count(), 1)
        inactive_agents = Agent.objects.inactive()
        self.assertEquals(inactive_agents.count(), 0)

class PersonaTestCase(TestCase):
    def test_persona(self):
        self.assertEquals(Persona.objects.count(), 0)
        Persona.objects.create(name="Analytical")
        self.assertEquals(Persona.objects.count(), 1)