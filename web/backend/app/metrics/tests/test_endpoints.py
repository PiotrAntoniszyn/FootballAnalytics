from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from teams.tests.factories import PlayerFactory

from .factories import MetricFactory


class TestMetricsEndpoint(APITestCase):
    def test_ok(self):
        metric_1 = MetricFactory(
            internal_name="Gls", display_name="Goals", group="radar"
        )
        metric_2 = MetricFactory(
            internal_name="xG", display_name="Expected Goals", group="radar"
        )

        url = reverse("get_radar_metrics")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_response = [
            {"id": metric_1.id, "display_name": metric_1.display_name},
            {"id": metric_2.id, "display_name": metric_2.display_name},
        ]
        self.assertEqual(response.json(), expected_response)


class TestRadarChartEndpoint(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.player = PlayerFactory()
        cls.metric_1 = MetricFactory(
            internal_name="Gls", display_name="Goals", group="radar"
        )
        cls.metric_2 = MetricFactory(
            internal_name="xG", display_name="Expected Goals", group="radar"
        )
        MetricFactory(internal_name="Ast", display_name="Assists", group="radar")

    def test_no_metrics(self):
        url = reverse("get_radar_chart")
        response = self.client.get(url, data={"player_id": self.player.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected = {
            "metrics": ["0", "0", "0"],
            "name": "Edouard Mendy",  # HACK: This is hardcoded until I fetch data from postgres
            "labels": ["Gls", "xG", "Ast"],
        }
        self.assertEqual(response.json(), expected)

    def test_selected_metrics(self):
        url = reverse("get_radar_chart")
        response = self.client.get(
            url,
            data={"player_id": 1, "metrics_ids": [self.metric_1.id, self.metric_2.id]},
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected = {
            "metrics": ["0", "0"],
            "name": "Edouard Mendy",
            "labels": ["Gls", "xG"],
        }
        self.assertEqual(response.json(), expected)

    def test_not_existing_player(self):
        url = reverse("get_radar_chart")
        response = self.client.get(url, data={"player_id": 2})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        expected = {
            "player_id": ["Player with id=2 does not exist"],
        }
        self.assertEqual(response.json(), expected)

    def test_invalid_metric(self):
        url = reverse("get_radar_chart")
        not_supported_metric = MetricFactory(
            internal_name="Ast", display_name="Assists", group="not-supported-metric"
        )
        response = self.client.get(
            url,
            data={
                "player_id": self.player.id,
                "metrics_ids": [not_supported_metric.id],
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        expected = {
            "metrics_ids": ["Unsupported metrics were passed to the endpoint."],
        }
        self.assertEqual(response.json(), expected)
