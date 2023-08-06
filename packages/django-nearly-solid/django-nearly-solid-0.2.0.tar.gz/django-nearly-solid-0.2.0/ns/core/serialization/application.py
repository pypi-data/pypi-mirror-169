from ns.core.entities.application import ApplicationData
from ns.core.serialization.entities import serialize_entities
from ns.core.serialization.services import serialize_services
from ns.core.typings import EntityMeta


def serialize_application(services: dict[str, type], entities: list[EntityMeta]) -> ApplicationData:
    return ApplicationData(
        services=serialize_services(**services),
        entities=serialize_entities(*entities),
    )

