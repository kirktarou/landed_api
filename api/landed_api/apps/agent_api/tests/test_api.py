from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework.views import status

from landed_api.apps.agent_api.models.agent import Agent, Persona, Region


class AgentListCreateAPIView(APITestCase):
    def setUp(self) -> None:
        self.url = reverse("api-agent-list", kwargs={"version": "v1"})

    def test_create_agent(self):
        self.assertEqual(Agent.objects.count(), 0)
        data = {
            "first_name": "Kirk",
            "last_name": "Tarou",
            "personas": ["Friendly"],
            "region": "Bay Area",
        }
        response = self.client.post(self.url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Agent.objects.count(), 1)
        self.assertEqual(Persona.objects.count(), 1)
        agent = Agent.objects.first()
        self.assertEqual(agent.first_name, data["first_name"])
        self.assertEqual(agent.last_name, data["last_name"])

    def test_get_agent_list(self):
        region = Region(name="Bay Area")
        region.save()
        agent = Agent(first_name="Kirk", last_name="Tarou", region=region)
        agent.save()
        persona = Persona(name="Friendly")
        persona.save()
        persona.agent.add(agent)

        response = self.client.get(self.url)
        response_json = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_json), 1)
        data = response_json[0]
        self.assertEqual(data["first_name"], agent.first_name)
        self.assertEqual(data["last_name"], agent.last_name)
        self.assertEqual(data["personas"][0], agent.personas.values()[0]["name"])


class AgentDetailsAPIViewTest(APITestCase):
    def setUp(self) -> None:
        region = Region(name="Bay Area")
        region.save()
        self.agent = Agent(first_name="Kirk", last_name="Tarou", region=region)
        self.agent.save()
        persona = Persona(name="Friendly")
        persona.save()
        persona.agent.add(self.agent)

        self.url = reverse("api-agent-details", kwargs={"version": "v1", "pk": self.agent.pk})

    def test_get_post_details(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data["pk"], str(self.agent.pk))
        self.assertEqual(data["first_name"], self.agent.first_name)
        self.assertEqual(data["last_name"], self.agent.last_name)
        self.assertEqual(data["personas"][0], self.agent.personas.values()[0]["name"])
        self.assertEqual(data["region"], self.agent.region.name)

    def test_update_agent(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        data["first_name"] = "Siobhán"
        data["last_name"] = "Cronin"
        data["region"] = "North Bay"
        data["personas"].append("Funny")
        self.assertEqual(Persona.objects.count(), 1)
        response = self.client.put(self.url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.agent.refresh_from_db()
        self.assertEqual(Persona.objects.count(), 2)
        self.assertEqual(self.agent.first_name, data["first_name"])
        self.assertEqual(self.agent.last_name, data["last_name"])
        self.assertEqual(self.agent.personas.values()[0]["name"], data["personas"][0])
        self.assertEqual(self.agent.personas.values()[1]["name"], data["personas"][1])
        self.assertEqual(self.agent.region.name, data["region"])

    def test_delete_agent(self):
        self.assertEqual(Agent.objects.count(), 1)
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Agent.objects.count(), 0)
