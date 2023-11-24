# generated by datamodel-codegen:
#   filename:  discriminator_in_array.yaml
#   timestamp: 2023-07-27T00:00:00+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import BaseModel, Field
from typing_extensions import Literal


class Type(Enum):
    my_first_object = 'my_first_object'
    my_second_object = 'my_second_object'


class ObjectBase(BaseModel):
    name: Optional[str] = Field(None, description='Name of the object')
    type: Literal['type1'] = Field(..., description='Object type')


class CreateObjectRequest(ObjectBase):
    name: str = Field(..., description='Name of the object')
    type: Literal['type2'] = Field(..., description='Object type')


class UpdateObjectRequest(ObjectBase):
    type: Literal['type3']


class MyArray(BaseModel):
    __root__: Union[ObjectBase, CreateObjectRequest, UpdateObjectRequest] = Field(
        ..., discriminator='type'
    )


class Demo(BaseModel):
    myArray: List[MyArray]
