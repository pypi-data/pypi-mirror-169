from dataclasses import dataclass
from typing import Optional

from dataclasses_json import dataclass_json

from telescope_sdk import SequenceStep
from telescope_sdk.common import UserFacingDataType


@dataclass_json
@dataclass
class Prospect(UserFacingDataType):
    campaign_id: str
    person_id: str
    first_name: str
    last_name: str
    company_name: str
    sequence_step_history: list[SequenceStep]
    job_title: Optional[str] = None
    email: Optional[str] = None
    average_sentiment: Optional[float] = None
