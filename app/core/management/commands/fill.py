import logging
from random import randint
from typing import Optional

from django.core.management import BaseCommand

from core.models import Human, Gender
from core.factory import HumanFactory

logger = logging.getLogger()

def create_family(counter: int,human: Optional[Human] = None, depth: int = 7):
    if depth == 0:
        return

    if human:
        commit_flag = False
        if not human.mother:
            commit_flag = True
            human.mother = HumanFactory(gender=Gender.FEMALE)
            counter += 1

        if not human.father:
            commit_flag = True
            human.father = HumanFactory(gender=Gender.MALE)
            counter += 1

        if commit_flag:
            human.save()

        mother = human.mother
        father = human.father
    else:
        mother = HumanFactory(gender=Gender.FEMALE)
        father = HumanFactory(gender=Gender.MALE)
        HumanFactory(mother=mother, father=father)

        counter += 3

    siblings_amount = randint(1, 6)
    humans = HumanFactory.create_batch(
        siblings_amount, mother=mother, father=father,
    )
    counter += len(humans)

    depth -= 1

    create_family(counter=counter, human=mother, depth=depth)
    create_family(counter=counter, human=father, depth=depth)


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--families', type=int)
        parser.add_argument('--depth', type=int)

    def handle(self, *args, **options):
        families = options['families']
        depth = options['depth']

        logger.info(f'Creating {families} families with depth {depth}')

        counter = 0
        for _ in range(families):
            create_family(depth=depth, counter=counter)

        logger.info(f'Created {counter} humans')
