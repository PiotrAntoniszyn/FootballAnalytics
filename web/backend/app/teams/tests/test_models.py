from django.test import TestCase

from .factories import PlayerFactory, TeamFactory


class TeamFactoryModelTests(TestCase):
    def test_model_creation(self):
        team = TeamFactory(name="Real Madrid")
        self.assertEqual(team.name, "Real Madrid")


class PlayerFactoryModelTests(TestCase):
    def test_model_creation(self):
        team = TeamFactory(name="Real Madrid")
        player = PlayerFactory(team=team, first_name="Andreas", last_name="Alonso")
        self.assertEqual(player.team, team)
        self.assertEqual(player.full_name, "Andreas Alonso")
