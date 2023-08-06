from typing import Any, Optional

from fastapi_camelcase import CamelModel
from pydantic import Field


class Coordinate(CamelModel):
    srs_code: Optional[str] = Field(..., alias="srsCode")
    latitude: float
    longitude: float
    location_accuracy_score: Optional[str] = Field(..., alias="locationAccuracyScore")
    location_provider: Optional[Any] = Field(..., alias="locationProvider")
    location_update_ts: Optional[str] = Field(..., alias="locationUpdateTs")
