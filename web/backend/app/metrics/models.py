from django.db import models


class Metric(models.base.Model):

    RADAR_GROUP = "radar"

    GROUP_CHOICES = [(RADAR_GROUP, "Radar Chart Metrics")]

    internal_name = models.CharField(max_length=256)
    display_name = models.CharField(max_length=256)
    group = models.CharField(max_length=256, choices=GROUP_CHOICES)

    def __str__(self):
        return f"({self.display_name} group={self.group})"
