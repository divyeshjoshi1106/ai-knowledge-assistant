import pytest
from app.services import document_service
from app.schemas.document import DocumentCreate


@pytest.fixture(autouse=True)
def reset_documents():
    document_service.documents.clear()
    document_service.next_id = 1

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

    assert result.id == 1
    assert result.filename == "My_file"
    assert result.description == "my new file"

def test_update_document():
    document = DocumentCreate(
        filename = "My_file",
        description = "my new file"
    )

    created = document_service.create_document(document)

    new_doc = DocumentCreate(
        filename = "New Name",
        description = "Updated file"
    )

    update = document_service.update_document(created.id, new_doc)

    assert created.filename == "New Name"
    assert created.description == "Updated file"

def test_delete_document():
    document = DocumentCreate(
        filename = "My_file",
        description = "my new file"
    )

    created = document_service.create_document(document)

    document_id = created.id

    message = document_service.delete_document(created.id)

    test_message = f"removed document with id: {document_id}"

    assert message["message"] == test_message