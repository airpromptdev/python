# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.



from .._models import BaseModel

__all__ = ["Prompt"]


class Prompt(BaseModel):
    model: str

    temperature: float

    text: str

    version: int
