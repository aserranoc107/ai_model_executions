from pydantic import BaseModel, Field

class ExecutionCreate(BaseModel):
    model_name: str = Field(min_length=1, max_length=100)
    input_tokens: int = Field(ge=0)
    output_tokens: int = Field(ge=0)
    execution_time_ms: int = Field(ge=0)
    cost_estimate: float = Field(ge=0)
    status: str = Field(min_length=1, max_length=20)
    executed_by: str | None = Field(default=None, max_length=100)