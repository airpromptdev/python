# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, TypedDict

__all__ = ["PromptGetParams"]


class PromptGetParams(TypedDict, total=False):
    version: Union[int, Literal["latest"]]
    """Version of prompt to return. 'latest' or a specific version number."""
