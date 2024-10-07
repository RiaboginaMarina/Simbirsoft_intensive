from pydantic import BaseModel


class Addition(BaseModel):
    additional_info: str = "Дополнительные сведения"
    additional_number: int = 123


class Entity(BaseModel):
    id: int | None = None
    addition: Addition
    important_numbers: list = [42, 21]
    title: str = "Заголовок сущности"
    verified: bool = True
