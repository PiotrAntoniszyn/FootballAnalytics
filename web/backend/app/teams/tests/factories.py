from factory import fuzzy
from factory.django import DjangoModelFactory
from teams.models import Player, Team


class PlayerFactory(DjangoModelFactory):
    class Meta:
        model = Player

    first_name = fuzzy.FuzzyChoice(["Timo", "Bob", "Andrew"])
    last_name = fuzzy.FuzzyChoice(["Verner", "Hawk", "Stark"])
    age = fuzzy.FuzzyInteger(18, 40)
    position = fuzzy.FuzzyChoice(["Goalkeeper", "Defence"])


class TeamFactory(DjangoModelFactory):
    class Meta:
        model = Team

    name = fuzzy.FuzzyText()
