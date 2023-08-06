from pydantic import BaseSettings, Field, HttpUrl


class WorkflowSettings(BaseSettings):
    RESPONSE_VERIFY_DICT: dict[str, str] = Field(
        default={},
        description="Response validation for elice API server.",
    )

    class Config:
        env_file = ".env.esbt"
        env_prefix = "esbt_"
