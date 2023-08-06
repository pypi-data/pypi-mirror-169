from dataclasses import dataclass

from ns.core.decorators import model
from ns.core.entities.methods import MethodData


@model
@dataclass
class ServiceData:
    __tech__ = True

    name: str
    methods: list[MethodData]
