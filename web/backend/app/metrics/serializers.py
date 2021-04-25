from metrics.models import Metric
from rest_framework import serializers
from teams.models import Player


class MetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metric
        fields = ["id", "display_name"]


class RadarChartSerializer(serializers.Serializer):

    player_id = serializers.IntegerField()
    metrics_ids = serializers.ListField(
        child=serializers.IntegerField(), allow_null=True
    )

    def validate_player_id(self, player_id):
        if not Player.objects.filter(id=player_id).exists():
            raise serializers.ValidationError(
                f"Player with id={player_id} does not exist"
            )
        return player_id

    def validate_metrics_ids(self, metrics_ids):
        # TODO: This should only return valid metric ids so it can be fetched from the database (?)
        if metrics_ids:
            metrics = Metric.objects.filter(
                id__in=metrics_ids, group="radar"
            ).values_list("internal_name", flat=True)
            if len(metrics) != len(metrics_ids):
                # TODO: I am lazy. This should be more descriptive.
                raise serializers.ValidationError(
                    f"Unsupported metrics were passed to the endpoint."
                )
            return metrics

        return Metric.objects.filter(group="radar").values_list(
            "internal_name", flat=True
        )
