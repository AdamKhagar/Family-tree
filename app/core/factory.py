from factory import Faker
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice

from core.models import Human, Gender


class HumanFactory(DjangoModelFactory):
    first_name = Faker('first_name')
    last_name = Faker('last_name')
    gender = FuzzyChoice(Gender.values)


    class Meta:
        model = Human