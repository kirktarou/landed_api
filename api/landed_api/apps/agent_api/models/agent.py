from django.db import models

from landed_api.apps.common.models import CoreModel


class Agent(CoreModel):
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.TextField(max_length=100, blank=False, null=False)
    first_time_agent = models.BooleanField(default=True, blank=False, null=False)

    class Meta:
        indexes = [
            models.Index(fields=["first_name"], name="agent_first_name_idx"),
            models.Index(fields=["last_name"], name="agent_last_name_idx"),
        ]
        ordering = ["last_name", "first_name"]
        unique_together = [["first_name", "last_name"]]

class Persona(models.Model):
    agent = models.ManyToManyField(
        Agent,
        related_name="personas",
        related_query_name="persona"
    )
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)

    def __str__(self):
        return self.name