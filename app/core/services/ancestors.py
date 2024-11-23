from typing import Optional, TypedDict

from core.models import Human

class HumanData(TypedDict):
    id: int
    first_name: str
    last_name: str
    mother: Optional['HumanData']
    father: Optional['HumanData']


def find_ancestors(human: Human, depth: Optional[int] = None) -> HumanData:
    human_data: HumanData = {
        'id': human.pk,
        'first_name': human.first_name,
        'last_name': human.last_name,
        'mother': None,
        'father': None,
    }

    if depth == 0:
        return human_data

    if depth is not None:
        depth -= 1

    human_data['mother'] = (
        find_ancestors(human.mother, depth=depth)
        if human.mother
        else None
    )
    human_data['father'] = (
        find_ancestors(human.father, depth=depth)
        if human.father
        else None
    )

    return human_data


