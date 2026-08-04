from app.schemas.document import Document, DocumentCreate
from app.database.memory import documents
from fastapi import HTTPException

next_id = 1


def get_document(document_id: int):
    for document in documents:
        if document.id == document_id:
            return document
    raise HTTPException(
        status_code=404,
        detail="Document doesn't exist"
    )



def create_document(document: DocumentCreate):
    global next_id

    new_document = Document(
        id=next_id, filename=document.filename, description=document.description
    )

    documents.append(new_document)

    next_id += 1
    return new_document


def delete_document(document_id: int):
    for document in documents:
        if document.id == document_id:
            documents.remove(document)
            return {"message": f"removed document with id: {document_id}"}
    raise HTTPException(
        status_code=404,
        detail="Document doesn't exist"
    )



def update_document(document_id: int, document: DocumentCreate):
    for doc in documents:
        if doc.id == document_id:
            doc.filename = document.filename
            doc.description = document.description
            return doc
    raise HTTPException(
        status_code=404,
        detail="Document doesn't exist"
    )
