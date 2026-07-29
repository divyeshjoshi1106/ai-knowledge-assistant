from app.services import document_service
from app.schemas.documents import DocumentCreate

def test_create_document():
    document = DocumentCreate(
        filename = "My_file",
        description = "my new file"
    )

    result = document_service.create_document(document)

    assert result.filename == "My_file"
    assert result.description == "my new file"

def test_get_document():
    document = DocumentCreate(
        filename = "My_file",
        description = "my new file"
    )

    created = document_service.create_document(document)

    result = document_service.get_document(created.id)

    assert result.filename == "My_file"
    assert result.description == "my new file"