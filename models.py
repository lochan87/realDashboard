from pydantic import BaseModel
from typing import List

class Dashboard(BaseModel):
    name: str
    widgets: List[str]