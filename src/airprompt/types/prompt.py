# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Prompt"]


class Prompt(BaseModel):
    model: Optional[str] = None

    prompt: Optional[str] = None

    temperature: Optional[float] = None

    version: Optional[int] = None
