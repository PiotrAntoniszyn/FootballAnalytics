from factory.django import DjangoModelFactory
from metrics.models import Metric


class MetricFactory(DjangoModelFactory):
    class Meta:
        model = Metric
