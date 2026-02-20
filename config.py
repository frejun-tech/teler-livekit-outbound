from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    LIVEKIT_URL: str
    LIVEKIT_API_KEY: str
    LIVEKIT_API_SECRET: str

    ROOM_NAME: str
    KRISP: bool
    WAIT_UNTIL_ANSWERED: bool

    SIP_TRUNK_ID: str
    SIP_CALL_TO: str
    AGENT_NAME: str

    class Config:
        env_file = ".env"


settings = Settings()