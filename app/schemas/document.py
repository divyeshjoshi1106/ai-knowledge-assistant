from pydantic import BaseModel


class DocumentCreate(BaseModel):
    filename: str
    description: str


class Document(DocumentCreate):
    id: int
