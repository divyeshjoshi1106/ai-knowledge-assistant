from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

documents = []
next_id = 1


class DocumentCreate(BaseModel):
    filename: str
    description: str


class Document(DocumentCreate):
    file_id: int


@router.get("/{document_id}")
def get_document(document_id: int):
    for document in documents:
        if document.file_id == document_id:
            return document
    return {"message": "document doesn't exist"}


@router.post("/")
def create_document(document: DocumentCreate):
    global next_id

    new_document = Document(
        file_id=next_id, filename=document.filename, description=document.description
    )

    documents.append(new_document)

    next_id += 1
    return new_document


@router.delete("/{document_id}")
def delete_document(document_id: int):
    for document in documents:
        if document.file_id == document_id:
            documents.remove(document)
            return {"message": f"removed document with id: {document_id}"}
    return {"message": "document doesn't exist"}


@router.put("/{document_id}")
def update_document(document_id: int, document: DocumentCreate):
    for doc in documents:
        if doc.file_id == document_id:
            doc.filename = document.filename
            doc.description = document.description
            return {"message": "document updated"}
    return {"message": "document doesn't exist"}
