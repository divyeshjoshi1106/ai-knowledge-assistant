from fastapi import APIRouter
from app.schemas.document import Document, DocumentCreate
from app.services import document_service

router = APIRouter()

@router.get("/{document_id}")
def get_document(document_id: int):
    return document_service.get_document(document_id)


@router.post("/")
def create_document(document: DocumentCreate):
    return document_service.create_document(document)


@router.delete("/{document_id}")
def delete_document(document_id: int):
    return document_service.delete_document(document_id)


@router.put("/{document_id}")
def update_document(document_id: int, document: DocumentCreate):
    return document_service.update_document(document_id, document)
