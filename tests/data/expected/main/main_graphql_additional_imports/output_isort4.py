# generated by datamodel-codegen:
#   filename:  additional-imports.graphql
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from datetime import date, datetime
from typing import Optional, TypeAlias

from pydantic import BaseModel, Field
from typing_extensions import Literal

from mymodule.myclass import MyCustomPythonClass

# The `Boolean` scalar type represents `true` or `false`.
Boolean: TypeAlias = bool


Date: TypeAlias = date


# DateTime (ISO8601, example: 2020-01-01T10:11:12+00:00)
DateTime: TypeAlias = datetime


MyCustomClass: TypeAlias = MyCustomPythonClass


# The `String` scalar type represents textual data, represented as UTF-8 character sequences. The String type is most often used by GraphQL to represent free-form human-readable text.
String: TypeAlias = str


class A(BaseModel):
    a: Date
    b: DateTime
    c: MyCustomClass
    typename__: Optional[Literal['A']] = Field('A', alias='__typename')
