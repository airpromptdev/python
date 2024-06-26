# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.



from .._models import BaseModel

__all__ = ["Prompt"]


class Prompt(BaseModel):
    model: str

    prompt: str

    temperature: float

    version: int
