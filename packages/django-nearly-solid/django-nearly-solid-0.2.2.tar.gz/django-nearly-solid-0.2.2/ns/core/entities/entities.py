from dataclasses import dataclass

from ns.core.decorators import model
from ns.core.entities.props import PropData
from ns.core.entities.types import TypeData


@model
@dataclass
class EntityData:
    __tech__ = True

    name: str
    type: TypeData
    props: list[PropData]

