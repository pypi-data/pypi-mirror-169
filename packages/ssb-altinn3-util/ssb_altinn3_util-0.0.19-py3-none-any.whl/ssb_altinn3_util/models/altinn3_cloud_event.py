import os
from pydantic import BaseModel, validator
from typing import Optional


class Altinn3CloudEvent(BaseModel):
    alternativesubject: str
    data: Optional[str]
    datacontenttype: Optional[str]
    id: str
    source: str
    specversion: str
    subject: str
    time: str
    type: str

    @validator("source")
    def validate_event_source(cls, v: str):
        expected: str = os.getenv("APPROVED_EVENT_SOURCE_URL")
        if not expected:
            raise ValueError(
                "Environment variable 'APPROVED_EVENT_SOURCE_URL' not found!"
            )
        options = expected.split(",")

        for option in options:
            if v.startswith(option):
                return v

        raise ValueError(
            f"Provided event source '{v}' did not match expected source '{expected}'"
        )
