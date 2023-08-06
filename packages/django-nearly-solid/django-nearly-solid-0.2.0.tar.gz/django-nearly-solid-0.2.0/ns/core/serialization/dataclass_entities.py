from dataclasses import Field, MISSING

from ns.core.entities.entities import EntityData
from ns.core.entities.props import PropData
from ns.core.serialization.types import serialize_type
from ns.core.typings import DataclassMeta


def serialize_dataclass_entity(model: DataclassMeta) -> EntityData:
    props = []
    for field_name, field in model.__dataclass_fields__.items():
        field: Field
        prop = PropData(
            name=field_name,
            type=serialize_type(field.type),
            required=field.default is MISSING,
            default_value=field.default,
        )
        props.append(prop)
    return EntityData(
        name=model.__name__,
        props=props,
        type=serialize_type(model),
    )
