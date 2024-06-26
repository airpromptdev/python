# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, TypedDict

__all__ = ["PromptRetrieveParams"]


class PromptRetrieveParams(TypedDict, total=False):
    version: Union[int, Literal["latest"]]
