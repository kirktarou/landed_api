import json

from django.core.management.base import BaseCommand, CommandError

from landed_api.apps.agent_api.models.agent import Agent, Persona, Region

class Command(BaseCommand):
    help = 'Load agents from JSON file'

    def add_arguments(self, parser):
        parser.add_argument('file', type=str)

    def handle(self, *args, **options):
        with open(options['file']) as f:
            data = json.load(f)
            agents = data['agents']
            for agent in agents:
                region_name = agent.pop('region')
                personas = agent.pop('personas')
                region, created = Region.objects.get_or_create(name=region_name)
                if created:
                    region.save()
                agent = Agent.objects.create(region=region, **agent)
                for persona in personas:
                    p, created = Persona.objects.get_or_create(name=persona)
                    p.agent.add(agent)
                    p.save()

