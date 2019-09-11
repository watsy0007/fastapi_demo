from pydantic import BaseModel
from typing import Any, Dict, List


class Default(BaseModel):
    code: int
    msg: str or None = None
    data: Any = []
