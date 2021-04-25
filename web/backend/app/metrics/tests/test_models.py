from django.test import TestCase

from .factories import MetricFactory


class MetricFactoryModelTests(TestCase):
    def test_model_creation(self):
        metric = MetricFactory(group="radar", display_name="Goals", internal_name="Gls")
        self.assertEqual(metric.group, "radar")
        self.assertEqual(metric.internal_name, "Gls")
        self.assertEqual(metric.display_name, "Goals")
