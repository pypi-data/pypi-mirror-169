from dataclasses import dataclass

from ns.core.decorators import model
from ns.core.entities.entities import EntityData
from ns.core.entities.services import ServiceData


@model
@dataclass
class ApplicationData:
    __tech__ = True

    services: list[ServiceData]
    entities: dict[str, EntityData]
