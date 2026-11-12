
from pydantic import BaseModel


class IntentionRequest(BaseModel):
    intention: str
