from dataclasses import dataclass
from inspect import Parameter

from ns.core.decorators import model
from ns.core.entities.types import TypeData


@model
@dataclass
class PropData:
    __tech__ = True

    name: str
    type: TypeData
    required: bool
    default_value: any = Parameter.empty
