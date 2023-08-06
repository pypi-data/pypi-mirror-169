from enum import Enum
from typing import List


class PartnersEnum(Enum):
    BELL_PARTNER = "Bell"
    ROGERS_PARTNER = "Rogers"
    VIDEOTRON_PARTNER = "Videotron"
    SHAW_PARTNER = "Shaw"


available_partners_list: List[str] = [partner.name for partner in PartnersEnum]
