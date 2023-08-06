from dataclasses import dataclass

from ns.core.decorators import model
from ns.core.entities.props import PropData
from ns.core.entities.types import TypeData


@model
@dataclass
class MethodData:
    __tech__ = True

    name: str
    args: list[PropData]
    return_type: TypeData
    auth_required: bool
    set_auth_token: bool
    upload_image: bool
    returns_png: bool
    is_query: bool
    description: str
