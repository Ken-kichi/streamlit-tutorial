import uuid
from pydantic import BaseModel,Field
from typing import Literal,Optional
from datetime import date

class Record(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    entry_type: Literal["Income","Expense"]
    category: Literal["Salary", "Food", "Transport", "Entertainment", "Other"]
    amount: float
    memo: Optional[str] = None
    date: date
