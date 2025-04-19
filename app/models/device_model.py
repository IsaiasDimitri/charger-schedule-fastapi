from sqlmodel import SQLModel, Field

class Device(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)